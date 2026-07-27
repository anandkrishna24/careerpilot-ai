from pathlib import Path
from uuid import uuid4
from app.services.gemini_service import GeminiService
from app.tools.resume_tool import ResumeTool

import fitz
from fastapi import UploadFile


class ResumeService:
    """
    Handles all resume-related operations.
    """

    # Folder where uploaded resumes will be stored
    UPLOAD_DIR = Path("uploads/resumes")

    def __init__(self):
        self.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        self.resume_tool = ResumeTool()

    async def save_resume(self, file: UploadFile):
        """
        Validates, saves the uploaded PDF and extracts its text.
        """

        # Validate file type
        if file.content_type != "application/pdf":
            return {
                "success": False,
                "message": "Only PDF files are allowed."
            }

        # Generate unique filename
        filename = f"{uuid4()}.pdf"

        # Full file path
        file_path = self.UPLOAD_DIR / filename

        # Save uploaded PDF
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Extract text from the saved PDF
        extracted_text = self.extract_text(file_path)

        analysis = self.resume_tool.analyze_resume(
            extracted_text
        )

        return {
            "success": True,
            "message": "Resume uploaded successfully.",
            "filename": filename,
            "analysis": analysis
        }

    def extract_text(self, file_path: Path):
        """
        Extracts text from the uploaded PDF.
        """

        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text