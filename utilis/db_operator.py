import json
import sqlite3
from models.sequence import Sequence


class PackageMeasurementHistory:
    def __init__(self, db_path):
        self.db_path = db_path
        self.create_table()

    def create_table(self):
        """
        Function to create the SQL database
        :return: the database connection object
        """
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS sequences (
                                id INTEGER PRIMARY KEY,
                                input_string TEXT,
                                measurements TEXT,
                                response TEXT,
                                time timestamp
                            )''')
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            if connection:
                connection.close()

    def save_curr_seq(self, sequence: Sequence) -> bool:
        """
        Function to insert the data coming from the requests to the SQL database
        :param sequence: the sequence of characters from user
        :return: a boolean value indicating whether the sequence was saved or not
        """
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO sequences (input_string, measurements, response, time) VALUES (?, ?, ?, ?)",
                (sequence.input_string, json.dumps(sequence.measurement),
                 sequence.response, sequence.time))
            connection.commit()

            # Clear input_string and measurements lists
            Sequence.input_string = ""
            Sequence.measurement = []

            return True
        except sqlite3.Error as e:
            print(f"Error saving sequence: {e}")
            return False
        finally:
            if connection:
                connection.close()

    def get_history(self) -> list:
        """
        Function to return the stored history from the SQL database
        :return: a list of history data including the string, measurements, error message, and response
        """
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            cursor.execute("SELECT input_string, measurements, time FROM sequences")
            rows = cursor.fetchall()

            return rows
        except sqlite3.Error as e:
            print(f"Error getting history: {e}")
            return {"status": "error", "data": None, "error": str(e)}
        finally:
            if connection:
                connection.close()

