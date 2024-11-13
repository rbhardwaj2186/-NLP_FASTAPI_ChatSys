import logging
import sqlite3
from datetime import datetime

class DatabaseHandler(logging.Handler):
    def __init__(self, db_name="logs.db"):
        super().__init__()
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                timestamp TEXT,
                level TEXT,
                message TEXT
            )
        ''')

    def emit(self, record):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        level = record.levelname
        message = record.getMessage()

        # Insert log record into database
        self.cursor.execute("INSERT INTO logs (timestamp, level, message) VALUES (?, ?, ?)",
                            (timestamp, level, message))
        self.conn.commit()

    def close(self):
        self.conn.close()
        super().close()

def setup_logging():
    logger = logging.getLogger("uvicorn")
    logger.setLevel(logging.INFO)
    db_handler = DatabaseHandler("logs/app_logs.db")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    db_handler.setFormatter(formatter)
    logger.addHandler(db_handler)
