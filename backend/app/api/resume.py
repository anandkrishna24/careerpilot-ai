from fastapi import APIRouter, File, UploadFile

from app.services.langgraph_service import LangGraphService
from app.services.resume_service import ResumeService


router = APIRouter()

resume_service = ResumeService()
langgraph_service = LangGraphService()


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    return await resume_service.save_resume(file)