from app.tools.career_tool import CareerTool


class CareerAgent:

    def __init__(self):

        self.career_tool = CareerTool()

    def generate_career_roadmap(
        self,
        resume_data,
        memory_context=""
    ):

        result = self.career_tool.generate_career_roadmap(
            resume_data
        )

        return result