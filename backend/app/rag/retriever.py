from pathlib import Path


class Retriever:

    DOCUMENTS_DIR = Path("app/rag/documents")

    def __init__(self):
        self.documents = self._load_documents()

    def _load_documents(self):

        documents = []

        if not self.DOCUMENTS_DIR.exists():
            return documents

        for file_path in self.DOCUMENTS_DIR.glob("*.txt"):

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()

            if content.strip():
                documents.append({
                    "source": file_path.name,
                    "content": content
                })

        return documents

    def retrieve(self, question, top_k=3):

        if not self.documents:
            return []

        question_words = set(
            question.lower().split()
        )

        scored_documents = []

        for document in self.documents:

            content_words = set(
                document["content"].lower().split()
            )

            score = len(
                question_words.intersection(content_words)
            )

            scored_documents.append(
                (score, document)
            )

        scored_documents.sort(
            key=lambda item: item[0],
            reverse=True
        )

        return [
            document
            for score, document
            in scored_documents[:top_k]
            if score > 0
        ]