import json

from app.services.gemini_service import GeminiService


class InterviewTool:

    def __init__(self):
        self.gemini = GeminiService()

    def generate_interview_questions(
        self,
        resume_data,
        career_data,
        learning_data,
        project_data,
        memory_context=""
    ):

        prompt = f"""
You are a Senior AI Technical Interviewer.

Based on the student's resume, career roadmap, learning plan, projects, and previous conversation context, generate personalised interview preparation.

Resume:

{json.dumps(resume_data, indent=2)}

Career Roadmap:

{json.dumps(career_data, indent=2)}

Learning Plan:

{json.dumps(learning_data, indent=2)}

Projects:

{json.dumps(project_data, indent=2)}

Previous Conversation Context:

{memory_context}

Use the previous conversation context only when it is relevant to the student's interview preparation.

Return ONLY valid JSON.

Schema:

{{
    "technical_questions": [],
    "python_questions": [],
    "sql_questions": [],
    "machine_learning_questions": [],
    "llm_questions": [],
    "hr_questions": [],
    "project_questions": [],
    "improvement_tips": []
}}
"""

        return self.gemini.generate(prompt)