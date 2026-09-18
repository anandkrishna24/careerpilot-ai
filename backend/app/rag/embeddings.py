from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingService:

    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name=self.MODEL_NAME
        )

    def get_embeddings(self):
        return self.embeddings