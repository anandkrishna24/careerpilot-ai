from app.database.memory_db import MemoryDatabase


class Memory:

    def __init__(self):

        self.database = MemoryDatabase()

    def add(self, role, content):

        self.database.save(
            role,
            content
        )

    def get_history(self):

        return self.database.get_all()

    def get_context(self, limit=10):

        history = self.database.get_all()

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

        self.database.clear()

    def close(self):

        self.database.close()