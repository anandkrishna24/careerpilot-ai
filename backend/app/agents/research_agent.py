from app.tools.research_tool import ResearchTool


class ResearchAgent:

    def __init__(self):

        self.research_tool = ResearchTool()

    def research(
        self,
        question,
        memory_context=""
    ):

        result = self.research_tool.research(
            question,
            memory_context
        )

        return result