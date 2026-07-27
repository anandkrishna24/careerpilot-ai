import json

from google import genai
from app.schemas.resume_schema import ResumeSchema
from app.schemas.career_schema import CareerSchema

from app.config.settings import GEMINI_API_KEY


class GeminiService:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def analyze_resume(self, resume_text: str):

        prompt = f"""
You are an expert ATS Resume Analyzer.

Analyse the following resume.

Return ONLY valid JSON.

Schema:

{{
    "name":"",
    "email":"",
    "phone":"",
    "skills":[],
    "education":[],
    "experience":[],
    "projects":[],
    "certifications":[]
}}

Resume:

{resume_text}
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        resume = ResumeSchema.model_validate(
            json.loads(text)
        )

        return resume.model_dump()
    def generate(self, prompt: str):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text