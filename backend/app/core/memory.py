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

    def clear(self):

        self.database.clear()

    def close(self):

        self.database.close()