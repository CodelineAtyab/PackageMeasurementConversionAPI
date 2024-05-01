import sqlite3
import threading

class SequenceHistory:
    def __init__(self, db_path='sequence_history.db'):
        self.db_path = db_path
        self.local_storage = threading.local()

    def get_connection(self):
        if not hasattr(self.local_storage, 'conn'):
            self.local_storage.conn = sqlite3.connect(self.db_path, check_same_thread=False)
            self.create_table()
        return self.local_storage.conn

    def create_table(self):
        conn = self.get_connection()
        query = '''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sequence TEXT NOT NULL,
            result TEXT NOT NULL
        );
        '''
        conn.execute(query)
        conn.commit()

    def add_entry(self, sequence, result):
        conn = self.get_connection()
        query = 'INSERT INTO history (sequence, result) VALUES (?, ?)'
        conn.execute(query, (sequence, str(result)))
        conn.commit()

    def get_history(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT sequence, result FROM history')
        return cursor.fetchall()

    def __del__(self):
        if hasattr(self.local_storage, 'conn'):
            self.local_storage.conn.close()
