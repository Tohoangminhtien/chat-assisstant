from agno.agent import Agent
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.agent import AgentKnowledge
from agno.embedder.google import GeminiEmbedder
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
import lancedb
import os


def rag(question: str) -> str:
    f"""
    Công cụ trả lời câu hỏi dựa vào kiến thức trong bộ nhớ theo cơ chế RAG (Retrieval Augmented Generation)

    Args:
        question (str): Câu hỏi cần được trả lời. Câu hỏi nên rõ ràng và liên quan đến dữ liệu trong bộ nhớ.
    Return:
        (str): câu trả lời từ mỗi file trong bộ nhớ
    """
    print("✅ Tool call: rag")

    # Load biến môi trường từ file env
    load_dotenv(dotenv_path="private/.env")
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    OPENAI_API_KEY = os.getenv('OPEN_AI_KEY')

    # Load knowledge
    db = lancedb.connect("tmp/lancedb")
    result = ""
    for table in db.table_names():
        knowledge_base = AgentKnowledge(
            vector_db=LanceDb(
                table_name=table,
                uri="tmp/lancedb",
                search_type=SearchType.vector,
                embedder=GeminiEmbedder(
                    id="text-embedding-004", api_key=GEMINI_API_KEY),
            ),
        )

        # Augumented
        agent = Agent(
            model=OpenAIChat(
                id="gpt-4o-mini",
                api_key=OPENAI_API_KEY,
                temperature=0.0
            ),
            knowledge=knowledge_base,
            search_knowledge=True
        )
        
        result+=f"Câu trả lời từ {table}: {agent.run(question).content}\n"
    
    return result
