import json
import sqlite3


class Sequence:
    def __init__(self, input_string, measurement):
        self.input_string = input_string
        self.measurement = measurement


class SequenceHistory:
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
                                error_message TEXT,
                                response TEXT
                            )''')
            connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            if connection:
                connection.close()

    def save_curr_seq(self, sequence: Sequence, error_message: str = None, response: str = None) -> bool:
        """
        Function to insert the data coming from the requests to the SQL database
        :param sequence: the sequence of characters from user
        :param error_message: in case of errors, an error message will be returned
        :param response: it states if the request is successful or  not
        :return: a boolean value indicating whether the sequence was saved or not
        """
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO sequences (input_string, measurements, error_message, response) VALUES (?, ?, ?, ?)",
                (sequence.input_string, json.dumps(sequence.measurement), error_message, response))
            connection.commit()

            # Clear input_string and measurements lists
            sequence.input_string = ""
            sequence.measurement = []

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
            cursor.execute("SELECT input_string, measurements, error_message, response FROM sequences")
            rows = cursor.fetchall()

            history = []
            for row in rows:
                data = {
                    'input_string': row[0],
                    'measurements': json.loads(row[1]),
                    'error_message': row[2],
                    'response': row[3]
                }
                history.append(data)

            return history
        except sqlite3.Error as e:
            print(f"Error getting history: {e}")
            return {"status": "error", "data": None, "error": str(e)}
        finally:
            if connection:
                connection.close()

