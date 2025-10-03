import os
from pathlib import Path
from raglite import RAGLiteConfig
from raglite import Document, insert_documents


my_config = RAGLiteConfig(
    db_url=os.getenv("DATABASE_URL"),
    llm=os.getenv("LLM", "gpt-4o-mini"),
    embedder=os.getenv("EMBEDDER", "text-embedding-3-large"),
)

documents = [
    Document.from_path(Path("Invoice_2345761353.pdf")),
]

insert_documents(documents, config=my_config)
