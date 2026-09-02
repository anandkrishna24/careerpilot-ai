from app.tools.interview_tool import InterviewTool


class InterviewService:

    def __init__(self):
        self.interview_tool = InterviewTool()

    def generate_interview_questions(
        self,
        resume_data,
        career_data,
        learning_data,
        project_data
    ):

        return self.interview_tool.generate_interview_questions(
            resume_data,
            career_data,
            learning_data,
            project_data
        )