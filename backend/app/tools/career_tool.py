from app.services.gemini_service import GeminiService


class CareerTool:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_career_roadmap(self, resume):

        prompt = f"""
You are an experienced AI Career Mentor.

Based on the following resume information, generate a structured career roadmap.

Resume:

{resume}

Return ONLY valid JSON.

Schema:

{{
    "career_goal": "",
    "current_level": "",
    "missing_skills": [],
    "recommended_certifications": [],
    "recommended_projects": [],
    "roadmap": [
        {{
            "month": 1,
            "goal": ""
        }}
    ]
}}
"""

        return self.gemini.generate(prompt)