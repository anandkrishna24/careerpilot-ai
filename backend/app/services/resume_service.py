from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile


class ResumeService:
    """
    Handles all resume upload operations.
    """

    # Folder where uploaded resumes will be stored
    UPLOAD_DIR = Path("uploads/resumes")

    def __init__(self):
        # Create the uploads/resumes folder if it doesn't exist
        self.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    async def save_resume(self, file: UploadFile):

        # Validate PDF
        if file.content_type != "application/pdf":
            return {
                "success": False,
                "message": "Only PDF files are allowed."
            }

        # Generate a unique filename
        filename = f"{uuid4()}.pdf"

        file_path = self.UPLOAD_DIR / filename

        # Save the uploaded file
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        return {
            "success": True,
            "message": "Resume uploaded successfully.",
            "filename": filename
        }