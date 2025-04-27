import lancedb
import re
from dotenv import load_dotenv
import os
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.embedder.google import GeminiEmbedder


def load_knowledge(pdf_file: str) -> str:
    """
    Hàm đọc file pdf và lưu trữ dưới dạng LanceDB
    Return:
        Thông báo đã cập nhật hoặc đã tồn tại.
    """
    # Load biến môi trường từ file env
    load_dotenv(dotenv_path="private/.env")
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    table_name = re.search(r'([^/\\]+?)(?:\.[^.]*$|$)', pdf_file).group(1)

    # Mở database từ đường dẫn local
    db = lancedb.connect("tmp/lancedb")
    if table_name in db.table_names():
        return f"Dữ liệu về {table_name} đã tồn tại!"

    # else:
    # Embedder
    embeddings = GeminiEmbedder(
        id="text-embedding-004", api_key=GEMINI_API_KEY)

    # Vector DB
    vector_db = LanceDb(
        uri="tmp/lancedb",
        table_name=table_name,
        search_type=SearchType.hybrid,
        embedder=embeddings,
    )

    # Load knowledge
    knowledge_base = PDFKnowledgeBase(
        path=pdf_file,
        vector_db=vector_db,
    )

    knowledge_base.load()
    return f"Đã cập nhật bộ nhớ cho file {table_name}"
