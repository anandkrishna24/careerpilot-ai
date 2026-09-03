from fastapi import APIRouter

from app.services.langgraph_service import LangGraphService


router = APIRouter()

langgraph_service = LangGraphService()


@router.post("/roadmap")
async def generate_career_roadmap(data: dict):
    result = langgraph_service.execute(
        request_type="career",
        data=data
    )

    return {
        "success": True,
        "result": result.get("result"),
        "memory_context": result.get("memory_context", "")
    }