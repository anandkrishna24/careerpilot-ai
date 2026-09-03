from langgraph.graph import END, START, StateGraph

from app.agents.graph_state import CareerPilotState
from app.agents.supervisor_agent import SupervisorAgent


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

    graph.add_edge(START, "supervisor")
    graph.add_edge("supervisor", END)

    return graph.compile()