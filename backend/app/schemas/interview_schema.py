from typing import List

from pydantic import BaseModel


class InterviewSchema(BaseModel):

    technical_questions: List[str]

    python_questions: List[str]

    sql_questions: List[str]

    machine_learning_questions: List[str]

    llm_questions: List[str]

    hr_questions: List[str]

    project_questions: List[str]

    improvement_tips: List[str]