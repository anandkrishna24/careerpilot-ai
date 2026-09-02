from app.tools.resume_tool import ResumeTool


class ResumeAgent:

    def __init__(self):
        self.resume_tool = ResumeTool()

    def analyze_resume(self, resume_text: str):

        result = self.resume_tool.analyze_resume(
            resume_text
        )

        return result