from typing import List

from pydantic import BaseModel


class ProjectSchema(BaseModel):

    beginner_projects: List[str]

    intermediate_projects: List[str]

    advanced_projects: List[str]

    recommended_github_structure: List[str]

    deployment_suggestions: List[str]