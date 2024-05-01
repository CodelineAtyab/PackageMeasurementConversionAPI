import cherrypy
import sqlite3
from services.measurement_service import convert_measurements  # Ensure this module and function are correctly implemented.
import logging

DATABASE_NAME = "measurements.db"

class MeasurementAPI:
    def __init__(self):
        self.create_table()

    def connect(self):
        return sqlite3.connect(DATABASE_NAME)

    def create_table(self):
        with self.connect() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    input_str TEXT NOT NULL,
                    output_str TEXT NOT NULL
                );
            ''')

    def add_to_history(self, input_str, output_str):
        try:
            with self.connect() as conn:
                conn.execute('INSERT INTO history (input_str, output_str) VALUES (?, ?)', (input_str, output_str))
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

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def convert(self, input_str=""):
        if not input_str:
            return {"error": "No input provided"}
        result = convert_measurements(input_str)
        self.add_to_history(input_str, str(result))
        return {"input": input_str, "output": result}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def history(self):
        return {"history": self.get_history()}
    