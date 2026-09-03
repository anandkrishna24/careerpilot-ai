from app.services.gemini_service import GeminiService


class ResumeTool:
    """
    Tool responsible for analysing resumes using Gemini.
    """

    def __init__(self):
        self.gemini = GeminiService()

    def analyze_resume(
        self,
        resume_text: str,
        memory_context=""
    ):
        return self.gemini.analyze_resume(
            resume_text,
            memory_context
        )