import json

from app.services.gemini_service import GeminiService


class LearningTool:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_learning_plan(
        self,
        career_data,
        memory_context=""
    ):

        prompt = f"""
You are an experienced AI Learning Mentor.

Based on the following career roadmap and previous conversation context, generate a personalised learning plan.

Career Roadmap:

{json.dumps(career_data, indent=2)}

Previous Conversation Context:

{memory_context}

Use the previous conversation context only when it is relevant to the student's learning plan.

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
"""

        return self.gemini.generate(prompt)