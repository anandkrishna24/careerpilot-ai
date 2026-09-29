class ResearchTool:

    def __init__(self):
        self.rag_pipeline = None

    def research(self, question, memory_context=""):

        if self.rag_pipeline is None:
            from app.rag.rag_pipeline import RAGPipeline

            self.rag_pipeline = RAGPipeline()

        result = self.rag_pipeline.research(
            question,
            memory_context
        )

        return result