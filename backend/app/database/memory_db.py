import sqlite3
from pathlib import Path


class MemoryDatabase:
    DB_PATH = Path("app/database/memory.db")

    def __init__(self):
        self.DB_PATH.parent.mkdir(parents=True, exist_ok=True)

        self.connection = sqlite3.connect(self.DB_PATH)

        self._create_table()

    def _create_table(self):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            PRAGMA table_info(memory)
            """
        )

        columns = [row[1] for row in cursor.fetchall()]

        # Existing database created before session support
        if columns and "session_id" not in columns:
            cursor.execute(
                """
                ALTER TABLE memory
                ADD COLUMN session_id TEXT NOT NULL DEFAULT 'default'
                """
            )

        # New database
        elif not columns:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL
                )
                """
            )

        self.connection.commit()

    def save(self, session_id, role, content):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO memory (
                session_id,
                role,
                content
            )
            VALUES (?, ?, ?)
            """,
            (session_id, role, content)
        )

        self.connection.commit()

    def get_all(self, session_id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT role, content
            FROM memory
            WHERE session_id = ?
            ORDER BY id
            """,
            (session_id,)
        )

        rows = cursor.fetchall()

        return [
            {
                "role": role,
                "content": content
            }
            for role, content in rows
        ]

    def clear(self, session_id):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            DELETE FROM memory
            WHERE session_id = ?
            """,
            (session_id,)
        )

        self.connection.commit()

    def close(self):
        self.connection.close()