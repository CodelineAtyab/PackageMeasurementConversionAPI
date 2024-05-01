import cherrypy
from models.database_initializer import init_db
from models.sequence_output import SequenceOutput


class ConversionDatabaseOperations:

    @staticmethod
    def get_db():
        """
        A function that retrieves the database connection object, and initializing it if it is not present
        :return: A database connection object
        """
        if not hasattr(cherrypy.thread_data, 'conn'):
            cherrypy.thread_data.conn = init_db()
        return cherrypy.thread_data.conn

    def save_to_db(self, m: SequenceOutput, converted_result):
        """
        A function to save conversion data to the database
        :param m: User sequence object containing user_input, converted_result, status, error_message
        :param converted_result: Converted result string or list
        """
        with self.get_db() as conn:
            cursor = conn.cursor()
            if isinstance(converted_result, list):
                converted_result = ', '.join(str(item) for item in converted_result)
            cursor.execute('''INSERT INTO conversions (user_input, converted_result, status, error_message)
                              VALUES (?, ?, ?, ?)''',
                           (m.user_input, m.converted_result, m.status, ""))
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
