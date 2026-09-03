from app.agents.careerpilot_graph import build_careerpilot_graph


class LangGraphService:
    def __init__(self):
        self.graph = build_careerpilot_graph()

    def execute(self, request_type, data, session_id="default"):
        state = {
            "request_type": request_type,
            "data": data,
            "session_id": session_id
        }

        return self.graph.invoke(state)
    