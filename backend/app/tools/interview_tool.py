import json

from app.prompts.interview_prompt import get_interview_prompt
from app.services.gemini_service import GeminiService


class InterviewTool:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_interview_questions(
        self,
        resume_data,
        career_data,
        learning_data,
        project_data
    ):

        prompt = get_interview_prompt(
            json.dumps(resume_data, indent=2),
            json.dumps(career_data, indent=2),
            json.dumps(learning_data, indent=2),
            json.dumps(project_data, indent=2)
        )

        return self.gemini.generate(prompt)