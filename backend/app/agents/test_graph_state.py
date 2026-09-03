from app.agents.graph_state import CareerPilotState


state: CareerPilotState = {
    "request_type": "career",
    "data": {
        "skills": ["Python", "SQL"],
        "education": ["PG Diploma"]
    },
    "session_id": "sprint69_test"
}

assert state["request_type"] == "career"
assert state["data"]["skills"] == ["Python", "SQL"]
assert state["data"]["education"] == ["PG Diploma"]
assert state["session_id"] == "sprint69_test"

print("CareerPilotState validation successful")
print(state)