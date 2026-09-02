from fastapi import APIRouter, File, UploadFile

from app.services.resume_service import ResumeService

router = APIRouter()

resume_service = ResumeService()


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    return await resume_service.save_resume(file)
