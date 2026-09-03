import sqlite3
from pathlib import Path


class MemoryDatabase:

    DB_PATH = Path("app/database/memory.db")

    def __init__(self):

        self.DB_PATH.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.connection = sqlite3.connect(
            self.DB_PATH
        )

        self._create_table()

    def _create_table(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role TEXT NOT NULL,
                content TEXT NOT NULL
            )
            """
        )

        self.connection.commit()

    def save(self, role, content):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO memory (role, content)
            VALUES (?, ?)
            """,
            (role, content)
        )

        self.connection.commit()

    def get_all(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT role, content
            FROM memory
            ORDER BY id
            """
        )

        rows = cursor.fetchall()

        return [
            {
                "role": role,
                "content": content
            }
            for role, content in rows
        ]

    def clear(self):

        cursor = self.connection.cursor()

        cursor.execute(
            "DELETE FROM memory"
        )

        self.connection.commit()

    def close(self):

        self.connection.close()