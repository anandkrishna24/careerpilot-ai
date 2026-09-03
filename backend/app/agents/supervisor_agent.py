from app.agents.resume_agent import ResumeAgent
from app.agents.career_agent import CareerAgent
from app.agents.learning_agent import LearningAgent
from app.agents.project_agent import ProjectAgent
from app.agents.interview_agent import InterviewAgent
from app.agents.research_agent import ResearchAgent
from app.core.memory import Memory


class SupervisorAgent:

    def __init__(self):

        self.resume_agent = ResumeAgent()
        self.career_agent = CareerAgent()
        self.learning_agent = LearningAgent()
        self.project_agent = ProjectAgent()
        self.interview_agent = InterviewAgent()
        self.research_agent = ResearchAgent()

        self.memory = Memory()

    def route(self, request_type, data):

        context = self.memory.get_context()

        self.memory.add(
            "user",
            str(data)
        )

        if request_type == "resume":

            result = self.resume_agent.analyze_resume(
                data,
                context
            )

        elif request_type == "career":

            result = self.career_agent.generate_career_roadmap(
                data,
                context
            )

        elif request_type == "learning":

            result = self.learning_agent.generate_learning_plan(
                data,
                context
            )

        elif request_type == "project":

            result = self.project_agent.generate_projects(
                data["resume_data"],
                data["career_data"],
                context
            )

        elif request_type == "interview":

            result = self.interview_agent.generate_interview_questions(
                data["resume_data"],
                data["career_data"],
                data["learning_data"],
                data["project_data"],
                context
            )

        elif request_type == "research":

            result = self.research_agent.research(
                data,
                context
            )

        else:

            result = {
                "success": False,
                "message": "Unknown request type."
            }

        self.memory.add(
            "assistant",
            str(result)
        )

        return {
            "success": True,
            "memory_context": context,
            "result": result
        }