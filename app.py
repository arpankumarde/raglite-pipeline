import os
from raglite import RAGLiteConfig


my_config = RAGLiteConfig(
    db_url=os.getenv("DATABASE_URL"),
    llm=os.getenv("LLM", "gpt-4o-mini"),
    embedder=os.getenv("EMBEDDER", "text-embedding-3-large"),
)
