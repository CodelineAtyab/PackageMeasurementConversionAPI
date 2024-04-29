import sqlite3

from src.abstraction.dataformat import DataFormat
from src.models.sequence import Sequence


class SQLDataFormat(DataFormat):
    db_path = './src/data/sequence_history.db'  # Define the database path at the class level if constant

    @staticmethod
    def connect():
        """
        Establish a connection to the SQLite database.
        """
        return sqlite3.connect(SQLDataFormat.db_path)

    def format(self, input_string: Sequence):
        """
        Insert the input string into the SQLite database with the current timestamp.
        """
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sequence_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    input_string TEXT,
                    created_at TEXT
                );
            ''')
            cursor.execute('INSERT INTO sequence_history (input_string, created_at) VALUES (?, ?)',
                           (input_string.get_string(), input_string.created_at))
            conn.commit()
        return f"Data inserted: {input_string.get_string()} at {input_string.created_at}" + "\n"
