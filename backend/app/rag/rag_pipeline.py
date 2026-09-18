from app.rag.retriever import Retriever
from app.prompts.research_prompt import get_research_prompt
from app.services.gemini_service import GeminiService


class RAGPipeline:

    def __init__(self):
        self.retriever = Retriever()
        self.gemini = GeminiService()

    def research(self, question, memory_context=""):

        documents = self.retriever.retrieve(
            question,
            top_k=3
        )

        if not documents:
            return {
                "success": False,
                "message": "No relevant research information found."
            }

        context_parts = []

        for document in documents:
            context_parts.append(
                f"Source: {document['source']}\n"
                f"Content:\n{document['content']}"
            )

        context = "\n\n".join(context_parts)

        prompt = get_research_prompt(
            question,
            context
        )

        if memory_context:
            prompt += f"""

Previous Conversation Context:

{memory_context}

Use the previous conversation context only when it is relevant.
"""

        answer = self.gemini.generate(prompt)

        sources = list(dict.fromkeys(
            document["source"]
            for document in documents
        ))

        return {
            "success": True,
            "question": question,
            "answer": answer,
            "sources": sources
        }