import json

from app.services.gemini_service import GeminiService


class ProjectTool:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_projects(
        self,
        resume_data,
        career_data,
        memory_context=""
    ):

        prompt = f"""
You are an experienced AI Project Mentor.

Based on the following resume information, career roadmap, and previous conversation context, recommend suitable projects for the student.

Resume:

{json.dumps(resume_data, indent=2)}

Career Roadmap:

{json.dumps(career_data, indent=2)}

Previous Conversation Context:

{memory_context}

Use the previous conversation context only when it is relevant to the student's project recommendations.

Return ONLY valid JSON.

Schema:

{{
    "beginner_projects": [],
    "intermediate_projects": [],
    "advanced_projects": [],
    "recommended_github_structure": [],
    "deployment_suggestions": []
}}
"""

        return self.gemini.generate(prompt)