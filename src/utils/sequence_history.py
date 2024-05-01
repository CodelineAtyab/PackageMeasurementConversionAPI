from src.models.sequence import Sequence


import sqlite3
from datetime import datetime


class SequenceHistoryModel:
    def __init__(self, db_path="./src/data/sequence_history.db"):
        self.db_path = db_path
        self.data = []
        self.load_sequences()

    def connect(self):
        """
        Establish a connection to the SQLite database.
        """
        return sqlite3.connect(self.db_path)

    def fetch_sequences_from_db(self):
        """
        Fetches all sequences from the database and returns them as a list of dictionaries.
        """
        sequences = []
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT input_string, created_at FROM sequence_history")
                rows = cursor.fetchall()
                for row in rows:
                    formatted = datetime.fromtimestamp(float(row[1])).strftime("%Y-%m-%d %H:%M:%S")
                    sequences.append({'input_string': row[0], 'created_at': formatted})
            return sequences
        except FileNotFoundError as file:
            print("File Not found")
        except Exception as ex:
            print("Error", ex)

    def load_sequences(self):
        """
        Load sequences from the database into the model.
        """
        try:
            sequences_from_db = self.fetch_sequences_from_db()
            for seq in sequences_from_db:
                sequence = Sequence(seq['input_string'], seq['created_at'])
                self.data.append(sequence)
        except Exception as ex:
            print("Error", ex)
