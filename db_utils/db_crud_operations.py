import sqlite3
import logging
from services.measurement_service import convert_measurements  # Ensure this module and function are correctly implemented.
from models.processed_result import ProcessResult

import cherrypy


DATABASE_NAME = "measurements.db"

class DbCrudOpearations:

    def __init__(self):
        self.create_table()

    def connect(self):
        return sqlite3.connect(DATABASE_NAME)

    def create_table(self):
        
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    input_str TEXT NOT NULL,
                    output_str TEXT NOT NULL
                );
            ''')

    def add_to_history(self, processed_res_obj: ProcessResult):
        try:
            with self.connect() as conn:
                conn.execute('INSERT INTO history (input_str, output_str) VALUES (?, ?)', (processed_res_obj.given_seq, processed_res_obj.generated_seq))
        except sqlite3.DatabaseError as e:
            logging.error(f"Database error: {e}")
            # Optionally, re-raise or handle the error differently
            raise

    def get_history(self):
        try:
            with self.connect() as conn:
                cursor = conn.execute('SELECT input_str, output_str FROM history')
                return [{"input": row[0], "output": row[1]} for row in cursor.fetchall()]
        except sqlite3.DatabaseError as e:
            logging.error(f"Database error: {e}")
            return []