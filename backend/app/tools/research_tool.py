from app.rag.rag_pipeline import RAGPipeline


class ResearchTool:

    def __init__(self):

        self.rag_pipeline = RAGPipeline()

    def research(self, question):

        result = self.rag_pipeline.research(
            question
        )

        return result