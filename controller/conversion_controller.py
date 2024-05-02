import json
import cherrypy
from services.conversion_service import Conversion
from models.database_initializer import init_db
from utilis.database_operations import ConversionDatabaseOperations
from models.sequence_output import SequenceOutput


class ConversionController:

    class MeasurementConversion:

        def __init__(self):
            self.converter = Conversion()  # Instantiate the Conversion class

        def convert_input(self, user_input):
            """
            A function to convert the user input to the list of values
            :param user_input: User input string
            :return: Converted result string or list
            """
            converted_result = self.converter.converted_string(user_input)  # Use the converted_string method
            return converted_result

    def __init__(self):
        self.controller = ConversionController.MeasurementConversion()
        self.conversion = Conversion()
        self.dbops = ConversionDatabaseOperations()

    @staticmethod
    def get_db():
        """
        A function that retrieves the database connection object, and initializing it if it is not present
        :return: A database connection object
        """
        if not hasattr(cherrypy.thread_data, 'conn'):
            cherrypy.thread_data.conn = init_db()
        return cherrypy.thread_data.conn

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def convert(self, user_input=None):
        """
        A function that exposes an endpoint to convert user's input to a converted list of values as JSON
        :param user_input: A sequence of characters that is None by default
        :return: A JSON response containing the conversion result, status, and error message
        """
        res_msg = {"status": "SUCCESS", "err_msg": "", "result": ""}
        m = SequenceOutput(user_input, None, None, None)
        try:
            if not user_input:
                user_input = cherrypy.request.params.get('user_input')
            if user_input is not None:
                converted_result = self.conversion.converted_string(user_input)
                m.user_input = user_input
                m.converted_result = str(converted_result)
                m.status = "SUCCESS"
                m.error_message = ""
                self.dbops.save_to_db(m, converted_result)
                res_msg["result"] = converted_result
            else:
                res_msg["status"] = "FAIL"
                res_msg["result"] = "Missing user_input parameter"
        except Exception as e:
            m.user_input = user_input
            m.converted_result = ""
            m.status = "ERROR"
            m.error_message = "ERROR"
            self.dbops.save_to_db(m, converted_result="")
            res_msg["status"] = "ERROR"
            res_msg["result"] = str(e)

        return res_msg

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_history(self):
        """
        A function that exposes an endpoint to retrieve conversions history
        :return: A JSON response containing conversion history
        """
        res_msg = {"status": "SUCCESS", "err_msg": "", "history": []}
        try:
            with self.get_db() as conn:
                cursor = conn.cursor()
                # Retrieve conversion history from SQLite
                cursor.execute('''SELECT * FROM conversions''')
                history = cursor.fetchall()
                res_msg["history"] = [
                    {"user_input": row[1], "converted_result": row[2], "status": row[3], "error_message": row[4]} for
                    row in history]
        except Exception as e:
            res_msg["status"] = "ERROR"
            res_msg["err_msg"] = str(e)
        return res_msg
