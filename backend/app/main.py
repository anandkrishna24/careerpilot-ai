from fastapi import FastAPI
from app.api.career import router as career_router
from app.api.resume import router as resume_router
from app.api.learning import router as learning_router
from app.api.project import router as project_router
from app.api.interview import router as interview_router

app = FastAPI(
    title="CareerPilot AI",
    version="1.0.0"
)

app.include_router(
    career_router,
    prefix="/career",
    tags=["Career"]
)

# Resume APIs
app.include_router(
    resume_router,
    prefix="/resume",
    tags=["Resume"]
)

@app.get("/")
def root():
    return {
        "message": "Welcome to CareerPilot AI 🚀"
    }

app.include_router(
    learning_router,
    prefix="/learning",
    tags=["Learning"]
)

app.include_router(
    project_router,
    prefix="/project",
    tags=["Project"]
)

app.include_router(
    interview_router,
    prefix="/interview",
    tags=["Interview"]
)

