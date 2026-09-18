from app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.vector_store = VectorStore()

    def retrieve(self, question, top_k=3):
        documents = self.vector_store.get_store().similarity_search(
            question,
            k=top_k
        )

        return [
            {
                "source": document.metadata.get("source", ""),
                "content": document.page_content
            }
            for document in documents
        ]