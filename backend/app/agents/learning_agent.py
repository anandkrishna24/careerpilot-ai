from app.tools.learning_tool import LearningTool


class LearningAgent:

    def __init__(self):

        self.learning_tool = LearningTool()

    def generate_learning_plan(
        self,
        career_data,
        memory_context=""
    ):

        result = self.learning_tool.generate_learning_plan(
            career_data,
            memory_context
        )

        return result