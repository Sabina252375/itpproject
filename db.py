import psycopg2
from config import DB_CONFIG

class Database:

    def __init__(self):
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor()
            self.init_db()
        except Exception as e:
            print("DB connection error:", e)

    def init_db(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS deadlines (
                id SERIAL PRIMARY KEY,
                user_id BIGINT,
                title TEXT,
                deadline TIMESTAMP,
                photo_id TEXT,
                notified_3d BOOLEAN DEFAULT FALSE,
                notified_2d BOOLEAN DEFAULT FALSE,
                notified_1d BOOLEAN DEFAULT FALSE,
                notified_10h BOOLEAN DEFAULT FALSE,
                notified_5h BOOLEAN DEFAULT FALSE,
                notified_1h BOOLEAN DEFAULT FALSE
            )
            """)
            self.conn.commit()
        except Exception as e:
            print("Init DB error:", e)

    def add_task(self, user_id, title, deadline, photo_id=None):
        try:
            self.cursor.execute("""
                INSERT INTO deadlines (user_id, title, deadline, photo_id,
                notified_3d, notified_2d, notified_1d, notified_10h, notified_5h, notified_1h)
                VALUES (%s, %s, %s, %s, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE)
                """, (user_id, title, deadline, photo_id))
            self.conn.commit()

        except Exception as e:
            print("Add task error:", e)

    def get_tasks(self, user_id):
        self.cursor.execute("SELECT * FROM deadlines WHERE user_id=%s ORDER BY deadline", (user_id,))
        return self.cursor.fetchall()

    def get_all(self):
        self.cursor.execute("SELECT * FROM deadlines")
        return self.cursor.fetchall()

    def delete_task(self, task_id):
        try:
            self.cursor.execute("DELETE FROM deadlines WHERE id=%s", (task_id,))
            self.conn.commit()
        except Exception as e:
            print("Delete error:", e)
