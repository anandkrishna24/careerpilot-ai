import json
import time

from google import genai

from app.config.settings import GEMINI_API_KEY
from app.schemas.resume_schema import ResumeSchema


class GeminiService:

    MODEL_NAME = "gemini-2.5-flash"

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def _generate_content(self, prompt: str):
        """
        Internal helper that retries Gemini requests if the service
        is temporarily unavailable.
        """

        retries = 3

        for attempt in range(retries):
            try:
                response = self.client.models.generate_content(
                    model=self.MODEL_NAME,
                    contents=prompt
                )

                return response.text

            except Exception as e:

                # Retry only if Gemini is temporarily unavailable
                if "503" in str(e) and attempt < retries - 1:
                    print(
                        f"Gemini busy... Retrying ({attempt + 1}/{retries})"
                    )
                    time.sleep(3)
                    continue

                raise e

    def analyze_resume(self, resume_text: str):

        prompt = f"""
You are an expert ATS Resume Analyzer.

Analyse the following resume.

Return ONLY valid JSON.

Schema:

{{
    "name": "",
    "email": "",
    "phone": "",
    "skills": [],
    "education": [],
    "experience": [],
    "projects": [],
    "certifications": []
}}

Resume:

{resume_text}
"""

        text = self._generate_content(prompt).strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        resume = ResumeSchema.model_validate(
            json.loads(text)
        )

        return resume.model_dump()

    def generate(self, prompt: str):
        """
        Generic Gemini method used by all Tools.
        """

        return self._generate_content(prompt)