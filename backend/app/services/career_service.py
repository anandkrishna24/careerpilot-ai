from app.tools.career_tool import CareerTool


class CareerService:

    def __init__(self):
        self.career_tool = CareerTool()

    def generate_roadmap(self, resume_data):

        return self.career_tool.generate_career_roadmap(
            resume_data
        )