from typing import Any, TypedDict


class CareerPilotState(TypedDict, total=False):
    request_type: str
    data: Any
    session_id: str
    memory_context: str
    result: Any