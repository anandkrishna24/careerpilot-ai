from google import genai

from app.config.settings import GEMINI_API_KEY


class EmbeddingService:

    MODEL_NAME = "gemini-embedding-2"
    DIMENSION = 768

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def _embed(self, text):
        response = self.client.models.embed_content(
            model=self.MODEL_NAME,
            contents=text,
            config={
                "output_dimensionality": self.DIMENSION
            }
        )

        return response.embeddings[0].values

    def embed_documents(self, texts):
        return [
            self._embed(text)
            for text in texts
        ]

    def embed_query(self, text):
        return self._embed(text)

    def get_embeddings(self):
        return self