import sqlite3

class Interaction:
    def __init__(self, id, question, answer):
        self.id = id
        self.question = question
        self.answer = answer

    def __repr__(self):
        return f"<Interaction id={self.id} question={self.question} answer={self.answer}>"

class Memory:
    def __init__(self, db_path='memory.db'):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row  # Pour récupérer les colonnes par nom
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def save_interaction(self, question, answer):
        self.cursor.execute(
            "INSERT INTO interactions (question, answer) VALUES (?, ?)",
            (question, answer)
        )
        self.conn.commit()

    def get_all_interactions(self):
        self.cursor.execute("SELECT id, question, answer FROM interactions")
        rows = self.cursor.fetchall()
        return [Interaction(row["id"], row["question"], row["answer"]) for row in rows]

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()
