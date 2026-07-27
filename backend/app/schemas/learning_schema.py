from typing import List

from pydantic import BaseModel


class WeeklyPlan(BaseModel):
    week: int
    goal: str


class LearningSchema(BaseModel):

    learning_path: List[str]

    recommended_courses: List[str]

    recommended_books: List[str]

    recommended_certifications: List[str]

    weekly_plan: List[WeeklyPlan]