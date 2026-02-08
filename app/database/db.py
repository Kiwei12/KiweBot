import sqlite3
from loguru import logger
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'animebot.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.init_db()

    def init_db(self):
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            schema = f.read()
        self.cursor.executescript(schema)
        self.conn.commit()
        logger.info('Database initialized.')

    def execute(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return self.cursor
        except Exception as e:
            logger.error(f"DB Error: {e}")
            return None

    def fetchall(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Exception as e:
            logger.error(f"DB Error: {e}")
            return []

    def fetchone(self, query, params=()):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except Exception as e:
            logger.error(f"DB Error: {e}")
            return None

    def close(self):
        self.conn.close()

# Singleton instance
DB = Database()
