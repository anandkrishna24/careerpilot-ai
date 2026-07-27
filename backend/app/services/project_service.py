from app.tools.project_tool import ProjectTool


class ProjectService:

    def __init__(self):
        self.project_tool = ProjectTool()

    def generate_projects(self, resume_data, career_data):

        return self.project_tool.generate_projects(
            resume_data,
            career_data
        )

    