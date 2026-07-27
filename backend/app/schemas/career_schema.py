from pydantic import BaseModel
from typing import List


class Roadmap(BaseModel):
    month: int
    goal: str


class CareerSchema(BaseModel):

    career_goal: str

    current_level: str

    missing_skills: List[str]

    recommended_certifications: List[str]

    recommended_projects: List[str]

    roadmap: List[Roadmap]