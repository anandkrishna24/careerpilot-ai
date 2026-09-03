from fastapi import APIRouter

from app.services.langgraph_service import LangGraphService


router = APIRouter()

langgraph_service = LangGraphService()


@router.post("/ask")
async def research_question(data: dict):
    question = data.get("question", "")

    result = langgraph_service.execute(
        request_type="research",
        data=question
    )

    return {
        "success": True,
        "result": result.get("result"),
        "memory_context": result.get("memory_context", "")
    }