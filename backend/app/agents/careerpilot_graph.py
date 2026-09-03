from langgraph.graph import END, START, StateGraph

from app.agents.graph_state import CareerPilotState
from app.agents.supervisor_agent import SupervisorAgent


VALID_REQUEST_TYPES = {
    "resume",
    "career",
    "learning",
    "project",
    "interview",
    "research",
}


def route_request(state: CareerPilotState):
    request_type = state.get("request_type")

    if request_type not in VALID_REQUEST_TYPES:
        raise ValueError(
            f"Unsupported request type: {request_type}"
        )

    return "supervisor"


def supervisor_node(state: CareerPilotState):
    supervisor = SupervisorAgent(
        session_id=state.get("session_id", "default")
    )

    result = supervisor.route(
        state["request_type"],
        state["data"]
    )

    return {
        "memory_context": result.get("memory_context", ""),
        "result": result.get("result")
    }


def build_careerpilot_graph():
    graph = StateGraph(CareerPilotState)

    graph.add_node("supervisor", supervisor_node)

    graph.add_edge(START, "router")

    graph.add_node("router", lambda state: state)

    graph.add_conditional_edges(
        "router",
        route_request,
        {
            "supervisor": "supervisor"
        }
    )

    graph.add_edge("supervisor", END)

    return graph.compile()