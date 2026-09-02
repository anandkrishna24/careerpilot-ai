from app.agents.resume_agent import ResumeAgent
from app.agents.career_agent import CareerAgent
from app.agents.learning_agent import LearningAgent
from app.agents.project_agent import ProjectAgent
from app.agents.interview_agent import InterviewAgent
from app.agents.research_agent import ResearchAgent


class SupervisorAgent:

    def __init__(self):

        self.resume_agent = ResumeAgent()
        self.career_agent = CareerAgent()
        self.learning_agent = LearningAgent()
        self.project_agent = ProjectAgent()
        self.interview_agent = InterviewAgent()
        self.research_agent = ResearchAgent()

    def route(self, request_type, data):

        if request_type == "resume":
            return self.resume_agent.analyze_resume(data)

        elif request_type == "career":
            return self.career_agent.generate_career_roadmap(data)

        elif request_type == "learning":
            return self.learning_agent.generate_learning_plan(data)

        elif request_type == "project":
            return self.project_agent.generate_projects(
                data["resume_data"],
                data["career_data"]
            )

        elif request_type == "interview":
            return self.interview_agent.generate_interview_questions(
                data["resume_data"],
                data["career_data"],
                data["learning_data"],
                data["project_data"]
            )

        elif request_type == "research":
            return self.research_agent.research(data)

        else:
            return {
                "success": False,
                "message": "Unknown request type."
            }