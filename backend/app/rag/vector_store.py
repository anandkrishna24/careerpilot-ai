from pathlib import Path

from langchain_chroma import Chroma

from app.rag.embeddings import EmbeddingService


class VectorStore:

    PERSIST_DIRECTORY = Path("app/rag/chroma_db")
    COLLECTION_NAME = "careerpilot_research"

    def __init__(self):
        self.PERSIST_DIRECTORY.mkdir(parents=True, exist_ok=True)

        embedding_service = EmbeddingService()

        self.vector_store = Chroma(
            collection_name=self.COLLECTION_NAME,
            embedding_function=embedding_service.get_embeddings(),
            persist_directory=str(self.PERSIST_DIRECTORY)
        )

    def get_store(self):
        return self.vector_store