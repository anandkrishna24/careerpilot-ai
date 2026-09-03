from app.services.gemini_service import GeminiService


class CareerTool:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_career_roadmap(
        self,
        resume,
        memory_context=""
    ):

        prompt = f"""
You are an experienced AI Career Mentor.

Based on the following resume information and previous conversation context, generate a structured career roadmap.

Resume:

{resume}

Previous Conversation Context:

{memory_context}

Use the previous conversation context only when it is relevant to the student's current career planning.

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