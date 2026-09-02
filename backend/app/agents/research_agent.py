from app.tools.research_tool import ResearchTool


class ResearchAgent:

    def __init__(self):

        self.research_tool = ResearchTool()

    def research(self, question):

        result = self.research_tool.research(
            question
        )

        return result