from app.tools.learning_tool import LearningTool


class LearningAgent:

    def __init__(self):
        self.learning_tool = LearningTool()

    def generate_learning_plan(self, career_data):

        result = self.learning_tool.generate_learning_plan(
            career_data
        )

        return result