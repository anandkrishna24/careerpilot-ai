def get_interview_prompt(
    resume_data,
    career_data,
    learning_data,
    project_data
):
    return f"""
You are a Senior AI Technical Interviewer.

Based on the student's profile, generate interview preparation.

Resume:
{resume_data}

Career Roadmap:
{career_data}

Learning Plan:
{learning_data}

Projects:
{project_data}

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