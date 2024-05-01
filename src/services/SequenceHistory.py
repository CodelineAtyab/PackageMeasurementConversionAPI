import sqlite3
import time
import datetime

# Manages Database Operations
class SequenceHistory:
    def __init__(self):
        self.db_name = "sequence_history.db"
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()


    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT, 
            input TEXT,
            status TEXT
        )
        '''
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def insert_data(self, status, input = "test"):
        insert_query = 'INSERT INTO history (datetime, input, status) VALUES (?, ?, ?)'
        data_to_insert = (str(time.time()), input, status)

        try:
            self.cursor.execute(insert_query, data_to_insert)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def fetch_data(self):
        select_query = 'SELECT * FROM history'

        try:
            # Fetch history from database and format it (epoch to human-readable time)
            self.cursor.execute(select_query)
            fetched_data = self.cursor.fetchall()
            filtered_data = []
            for entry in fetched_data:
                # Convert the timestamp to a datetime object and format it
                timestamp = float(entry[1])
                readable_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                # Append the converted time and the rest of the data, excluding the ID
                filtered_sublist = [readable_time, entry[2], entry[3]]
                filtered_data.append(filtered_sublist)
            return filtered_data
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None