import json
import cherrypy
from models.conversion import Conversion
from controller.app_controllers import MeasurementConversion, init_db


class MeasurementConversionHandler:
    exposed = True

    def __init__(self):
        self.controller = MeasurementConversion()
        self.conversion = Conversion()

    @staticmethod
    def get_db():
        """
        A function that retrieves the database connection object, and initializing it if it is not present
        :return: A database connection object
        """
        if not hasattr(cherrypy.thread_data, 'conn'):
            cherrypy.thread_data.conn = init_db()
        return cherrypy.thread_data.conn

    @cherrypy.tools.json_out()
    def __call__(self, user_input=None):
        """
        A function that exposes an endpoint to convert user's input to a converted list of values as JSON
        :param user_input: A sequence of characters that is None by default
        :return: A JSON response containing the conversion result, status, and error message
        """
        res_msg = {"status": "SUCCESS", "err_msg": "", "result": ""}
        try:
            if not user_input:
                user_input = cherrypy.request.params.get('user_input')
            if user_input is not None:
                converted_result = self.conversion.converted_string(user_input)
                self.controller.save_to_db(user_input, converted_result, "SUCCESS")
                res_msg["result"] = converted_result
            else:
                res_msg["status"] = "FAIL"
                res_msg["result"] = "Missing user_input parameter"
        except Exception as e:
            self.controller.save_to_db(user_input, "", "ERROR")
            res_msg["status"] = "ERROR"
            res_msg["result"] = str(e)

        return json.dumps(res_msg)

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
