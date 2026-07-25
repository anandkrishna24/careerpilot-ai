from fastapi import APIRouter
from app.services.career_service import CareerService

router = APIRouter()

career_service = CareerService()


@router.get("/info")
def get_project_information():
    return career_service.get_project_info()