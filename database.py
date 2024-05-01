import sqlite3


class Database:
    def __init__(self, db_name='conversion_history.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create the conversion_history table if it doesn't already exist."""
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS conversion_history (
            id INTEGER PRIMARY KEY,
            input TEXT,
            output TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        '''
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def save_conversion(self, input_str, output_str):
        """Save a conversion record to the database."""
        try:
            self.cursor.execute('INSERT INTO conversion_history (input, output) VALUES (?, ?)', (input_str, output_str))
            self.conn.commit()
            return True  # Return True if the operation was successful
        except sqlite3.Error as e:
            print(f"Error saving conversion: {e}")
            return False  # Return False if there was an error

    def fetch_conversion_history(self):
        """Retrieve the conversion history from the database."""
        try:
            self.cursor.execute("SELECT input, output FROM conversion_history ORDER BY timestamp DESC")
            rows = self.cursor.fetchall()
            conversion_history = [{'input': row[0], 'output': row[1]} for row in rows]
            return conversion_history
        except sqlite3.Error as e:
            print(f"Error fetching conversion history: {e}")
            return []

    def close_connection(self):
        """Close the database connection."""
        try:
            self.conn.close()
            print("Database connection closed.")
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")
