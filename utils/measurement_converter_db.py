import sqlite3
import json

class MeasurementConverterDB(object):
    def __init__(self, db_name='./data/history.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Create the table for the history of the measurements.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY,
                input TEXT,
                output TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def save_to_history(self, input_str, output_str):
        """
        Save the input and output to the history table.
        """
        output_str = str(output_str)
        self.cursor.execute('INSERT INTO history (input, output) VALUES (?, ?)', (input_str, output_str))
        self.conn.commit()
    
    def get_history(self):
        """
        Get the history of the measurements from the database.
        """
        self.cursor.execute("SELECT input, output FROM history ORDER BY timestamp DESC")
        rows = self.cursor.fetchall()
        history = [{'input': row[0], 'output': row[1]} for row in rows]
        return history

