import json

from app.services.gemini_service import GeminiService


class ProjectTool:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_projects(self, resume_data, career_data):

        prompt = f"""
You are a Senior AI Engineering Mentor.

Based on the student's resume and career roadmap, recommend portfolio projects.

Return ONLY valid JSON.

Schema:

{{
    "beginner_projects": [],
    "intermediate_projects": [],
    "advanced_projects": [],
    "recommended_github_structure": [],
    "deployment_suggestions": []
}}

Resume:

{json.dumps(resume_data, indent=2)}

Career Roadmap:

{json.dumps(career_data, indent=2)}
"""

        return self.gemini.generate(prompt)