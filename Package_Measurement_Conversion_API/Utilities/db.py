import sqlite3


class MeasurementsDB(object):
    def __init__(self, name_db='conversion_history.db'):
        self.name_db = name_db
        self.conn = sqlite3.connect(self.name_db, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):

        # Create the table that will store the conversion history
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversion_history (
                id INTEGER PRIMARY KEY,
                input TEXT,
                output TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def save_table(self, input_str, output_str):
        # Save the conversion history in the table
        output_str = str(output_str)
        self.cursor.execute('INSERT INTO conversion_history (input, output) VALUES (?, ?)', (input_str, output_str))
        self.conn.commit()

    def display_table(self):
        # Display the conversion history from the table
        conversion_history = []
        self.cursor.execute("SELECT input, output FROM conversion_history ORDER BY timestamp DESC")
        rows = self.cursor.fetchall()
        for row in rows:
            data = {'input': row[0], 'output': row[1]}
            conversion_history.append(data)
        # conversion_history = [{'input': row[0], 'output': row[1]} for row in rows]
        return conversion_history
