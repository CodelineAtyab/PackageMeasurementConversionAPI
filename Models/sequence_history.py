# sequence_history.py
import sqlite3

class SequenceHistory:
    def __init__(self, db_file):
        # Store the path to the SQLite database file
        self.db_file = db_file

    def save_sequence(self, sequence_data):
        # Connect to the SQLite database and save the sequence data
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            sequence = sequence_data['input']
            compressed_values = ','.join(map(str, sequence_data['compressed_values']))
            # Insert the sequence and compressed values into the 'sequences' table
            cursor.execute("INSERT INTO sequences (sequence, compressed_values) VALUES (?, ?)",
                            (sequence, compressed_values))
            conn.commit()

    def get_history(self):
        # Connect to the SQLite database and retrieve sequence history
        with sqlite3.connect(self.db_file) as conn:
            cursor = conn.cursor()
            # Execute SQL query to select sequences and order by timestamp in descending order
            cursor.execute("SELECT sequence, compressed_values, timestamp FROM sequences ORDER BY timestamp DESC")
            rows = cursor.fetchall()
            history = []
            # Iterate over rows and format data into a list of dictionaries
            for row in rows:
                history.append({
                    'sequence': row[0],
                    'compressed_values': list(map(int, row[1].split(','))),
                    'timestamp': row[2]
                })
            return history

