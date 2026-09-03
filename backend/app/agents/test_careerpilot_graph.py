from app.agents.careerpilot_graph import build_careerpilot_graph


graph = build_careerpilot_graph()

state = {
    "request_type": "career",
    "session_id": "langgraph_test_session",
    "data": {
        "skills": ["Python", "SQL"],
        "education": ["PG Diploma"]
    }
}

result = graph.invoke(state)

print("LangGraph execution successful")
print(result)