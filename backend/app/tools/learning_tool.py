import json

from app.services.gemini_service import GeminiService


class LearningTool:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_learning_plan(self, career_data):

        prompt = f"""
You are an experienced AI Learning Mentor.

Based on the following career roadmap, generate a personalised learning plan.

Return ONLY valid JSON.

Schema:

{{
    "learning_path": [],
    "recommended_courses": [],
    "recommended_books": [],
    "recommended_certifications": [],
    "weekly_plan": [
        {{
            "week": 1,
            "goal": ""
        }}
    ]
}}

Career Roadmap:

{json.dumps(career_data, indent=2)}
"""

        return self.gemini.generate(prompt)