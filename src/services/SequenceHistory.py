# from ..models.Sequence import Sequence
import os
import sqlite3
import time

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
            input TEXT 
        )
        '''
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def insert_data(self, input = "test"):
        insert_query = 'INSERT INTO history (datetime, input) VALUES (?, ?)'
        data_to_insert = (str(time.time()), input)

        try:
            self.cursor.execute(insert_query, data_to_insert)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def fetch_data(self):
        select_query = 'SELECT * FROM history'

        try:
            self.cursor.execute(select_query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None

    def close(self):
        self.conn.close()