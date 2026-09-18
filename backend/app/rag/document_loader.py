from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.rag.vector_store import VectorStore


class DocumentIngestion:

    DOCUMENTS_DIR = Path("app/rag/documents")

    def __init__(self):
        self.vector_store = VectorStore()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

    def load_documents(self):
        documents = []

        if not self.DOCUMENTS_DIR.exists():
            return documents

        for file_path in self.DOCUMENTS_DIR.glob("*.txt"):
            loader = TextLoader(
                str(file_path),
                encoding="utf-8"
            )

            documents.extend(loader.load())

        return documents

    def split_documents(self, documents):
        return self.text_splitter.split_documents(documents)

    def ingest(self):
        documents = self.load_documents()

        if not documents:
            return {
                "success": False,
                "message": "No research documents found.",
                "documents": 0,
                "chunks": 0
            }

        chunks = self.split_documents(documents)

        self.vector_store.get_store().add_documents(chunks)

        return {
            "success": True,
            "documents": len(documents),
            "chunks": len(chunks)
        }