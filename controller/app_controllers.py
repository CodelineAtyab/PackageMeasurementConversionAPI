import sqlite3
import cherrypy
from models.conversion import Conversion


def init_db():
    """
    A function to initialize the SQLite database
    :return: The database connection object
    """
    conn = sqlite3.connect('measurements.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS conversions
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      user_input TEXT,
                      converted_result TEXT,
                      status TEXT,
                      error_message TEXT)''')
    conn.commit()
    return conn


class MeasurementConversion:
    exposed = True

    def __init__(self):
        self.converter = Conversion()  # Instantiate the Conversion class

    @staticmethod
    def get_db():
        """
        A function that retrieves the database connection object, and initializing it if it is not present
        :return: A database connection object
        """
        if not hasattr(cherrypy.thread_data, 'conn'):
            cherrypy.thread_data.conn = init_db()
        return cherrypy.thread_data.conn

    def convert_input(self, user_input):
        """
        A function to convert the user input to the list of values
        :param user_input: User input string
        :return: Converted result string or list
        """
        converted_result = self.converter.converted_string(user_input)  # Use the converted_string method
        return converted_result

    def save_to_db(self, user_input, converted_result, status):
        """
        A function to save conversion data to the database
        :param user_input: User input string
        :param converted_result: Converted result string or list
        :param status: Status of the conversion
        """
        with self.get_db() as conn:
            cursor = conn.cursor()
            if isinstance(converted_result, list):
                converted_result = ', '.join(str(item) for item in converted_result)
            cursor.execute('''INSERT INTO conversions (user_input, converted_result, status, error_message)
                              VALUES (?, ?, ?, ?)''',
                           (user_input, converted_result, status, ""))
            conn.commit()

    def retrieve_history(self):
        """
        A function to retrieve conversion history from the database
        :return: List of conversion history entries
        """
        history = []
        try:
            with self.get_db() as conn:
                cursor = conn.cursor()
                cursor.execute('''SELECT * FROM conversions''')
                history = cursor.fetchall()
        except Exception as e:
            return e
            # print(f"An error occurred while retrieving history: {e}") # log statement to show the state of program
        return history
