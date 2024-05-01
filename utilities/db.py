import sqlite3
import logging
from models.sequence import Sequence
import json

class PackageMeasurementHistory:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS sequences (
                    id INTEGER PRIMARY KEY,
                    input_string TEXT,
                    measurements TEXT,
                    response TEXT,
                    time TIMESTAMP
                )
            ''')

    def save_curr_seq(self, sequence: Sequence) -> bool:
        """Save a Sequence object to the database."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    "INSERT INTO sequences (input_string, measurements, response, time) VALUES (?, ?, ?, ?)",
                    (sequence.input_string, json.dumps(sequence.measurement), sequence.response, sequence.time)
                )
            return True
        except sqlite3.Error as e:
            logging.error(f"Error saving sequence: {e}")
            return False
