from dotenv import load_dotenv
import os
import time
import gradio as gr
from agno.agent import Agent
from tool.website import summarize_website
from tool.news import get_news_lastest
from tool.rag import rag
from utils.common import *
from agno.models.openai import OpenAIChat

chat_history = []


def llm(message, history: list[dict], api_key, num_conversation=10) -> str:
    if message["files"]:
        file_path = message["files"][0]
        if str(file_path).endswith(".pdf"):
            return load_knowledge(file_path)
        else:
            return "Chỉ cho phép định dạng file .pdf"

    model = OpenAIChat(
        id="gpt-4o-mini",
        api_key=api_key,
        temperature=0.0
    )
    agent = Agent(model=model,
                  tools=[rag, summarize_website,
                         get_news_lastest])

    history.append({
        "question": message["text"],
        "answer": ""
    })
    conversation = ""
    for entry in history[-num_conversation:]:
        conversation += f"User: {entry['question']}\n"
        conversation += f"Chatbot: {entry['answer']}\n\n"

    result = agent.run(conversation).content
    history[-1]["answer"] = result
    return result


def process(message, history):
    # Load biến môi trường từ file env
    load_dotenv(dotenv_path="private/.env")
    key = os.getenv('OPEN_AI_KEY')
    result = llm(message, chat_history, api_key=key, num_conversation=10)
    temp = ""
    for i in str(result).split():
        time.sleep(0.05)
        temp += i + " "
        yield temp


print("* Running on local URL: http://localhost:7860/")
gr.ChatInterface(
    multimodal=True,
    fn=process,
    type="messages",
    fill_width=True,
    theme="soft",
    title="Chat Assisstant",
    save_history=True,
    stop_btn=False
).launch(server_name="0.0.0.0", quiet=True)