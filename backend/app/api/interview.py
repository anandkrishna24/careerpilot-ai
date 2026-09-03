from fastapi import APIRouter

from app.services.langgraph_service import LangGraphService


router = APIRouter()

langgraph_service = LangGraphService()


@router.post("/prepare")
async def generate_interview_preparation(data: dict):
    result = langgraph_service.execute(
        request_type="interview",
        data=data
    )

    return {
        "success": True,
        "result": result.get("result"),
        "memory_context": result.get("memory_context", "")
    }