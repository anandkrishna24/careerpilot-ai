from app.database.memory_db import MemoryDatabase


class Memory:

    def __init__(self, session_id="default"):

        self.session_id = session_id

        self.database = MemoryDatabase()

    def add(self, role, content):

        self.database.save(
            self.session_id,
            role,
            content
        )

    def get_history(self):

        return self.database.get_all(
            self.session_id
        )

    def get_context(self, limit=10):

        history = self.database.get_all(
            self.session_id
        )

        recent_history = history[-limit:]

        context = []

        for message in recent_history:

            context.append(
                f"{message['role']}: {message['content']}"
            )

        return "\n".join(context)

    def get_recent_context(self, limit=10):

        return self.get_context(limit)

    def clear(self):

        self.database.clear(
            self.session_id
        )

    def close(self):

        self.database.close()