from app.rag.rag_pipeline import RAGPipeline


class ResearchTool:
    def __init__(self):
        self.rag_pipeline = RAGPipeline()

    def research(self, question, memory_context=""):
        result = self.rag_pipeline.research(
            question,
            memory_context
        )

        return result