from app.rag.retriever import Retriever
from app.prompts.research_prompt import get_research_prompt
from app.services.gemini_service import GeminiService


class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.gemini = GeminiService()

    def research(self, question, memory_context=""):
        documents = self.retriever.retrieve(question)

        context = "\n\n".join(
            document["content"]
            for document in documents
        )

        if not context:
            return {
                "success": False,
                "message": "No relevant research information found."
            }

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

        return {
            "success": True,
            "question": question,
            "answer": answer
        }