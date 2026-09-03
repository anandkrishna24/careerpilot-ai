from pathlib import Path
from uuid import uuid4

import fitz
from fastapi import UploadFile

from app.services.langgraph_service import LangGraphService


class ResumeService:
    """
    Handles all resume-related operations.
    """

    # Folder where uploaded resumes will be stored
    UPLOAD_DIR = Path("uploads/resumes")

    def __init__(self):
        self.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        self.langgraph_service = LangGraphService()

    async def save_resume(self, file: UploadFile):
        """
        Validates, saves the uploaded PDF and extracts its text.
        LangGraph handles the resume analysis through the Supervisor Agent.
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

        # Execute resume analysis through LangGraph
        graph_result = self.langgraph_service.execute(
            request_type="resume",
            data=extracted_text
        )

        return {
            "success": True,
            "message": "Resume uploaded successfully.",
            "filename": filename,
            "resume_analysis": graph_result.get("result"),
            "memory_context": graph_result.get("memory_context", "")
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