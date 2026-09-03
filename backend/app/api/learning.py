from fastapi import APIRouter

from app.services.langgraph_service import LangGraphService


router = APIRouter()

langgraph_service = LangGraphService()


@router.post("/plan")
async def generate_learning_plan(data: dict):
    result = langgraph_service.execute(
        request_type="learning",
        data=data
    )

    return {
        "success": True,
        "result": result.get("result"),
        "memory_context": result.get("memory_context", "")
    }