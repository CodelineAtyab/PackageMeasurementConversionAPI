from src.models.sequence import Sequence


import sqlite3


class SequenceHistoryModel:
    def __init__(self, db_path="./src/data/sequence_history.db"):
        self.db_path = db_path
        self.data = []
        self.load_sequences()

    def connect(self):
        """ Establish a connection to the SQLite database. """
        return sqlite3.connect(self.db_path)

    def fetch_sequences_from_db(self):
        """
        Fetches all sequences from the database and returns them as a list of dictionaries.
        """
        sequences = []
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT input_string, created_at FROM sequence_history")
            rows = cursor.fetchall()
            for row in rows:
                sequences.append({'input_string': row[0], 'created_at': row[1]})
        return sequences

    def load_sequences(self):
        """Load sequences from the database into the model."""
        sequences_from_db = self.fetch_sequences_from_db()
        for seq in sequences_from_db:
            # Assuming Sequence class now has a method or way to also store processed time
            sequence = Sequence(seq['input_string'])
            sequence.processed_time = seq['created_at']  # Dynamically add processed time if not in constructor
            self.data.append(sequence)
