from app.tools.learning_tool import LearningTool


class LearningService:

    def __init__(self):
        self.learning_tool = LearningTool()

    def generate_learning_plan(self, career_data):

        return self.learning_tool.generate_learning_plan(
            career_data
        )