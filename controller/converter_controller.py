import cherrypy
from datetime import datetime

from services.package_converter import PackageConverter
from utilis.db_operator import PackageMeasurementHistory
from models.sequence import Sequence


class ConverterAPI:
    def __init__(self):
        self.converter = PackageConverter()
        self.sequence_history = PackageMeasurementHistory('./utilis/converter.db')

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def convert_measurements(self, input=None):
        """
        Function that exposes an API endpoint to convert the measurements given by user and handles the errors
        :param input: sequence of characters from user
        :return: a JSON response containing the status, response, measurements, and error
        """
        try:
            if input is None:
                input_string = cherrypy.request.params.get("input", "")

            input_string = input
            measurement = self.converter.package_measurement_conversion(input_string)
            time = datetime.now()
            if measurement != "Invalid":
                # Assuming no error message or response for now
                response = "Measurements saved successfully"
                sequence = Sequence(input_string, measurement, time, response)
                self.sequence_history.save_curr_seq(sequence)
                return {"status": "success", "err_msg": "", "result": measurement}
            else:
                error_message = "invalid sequence"
                response = "cant convert measurement input string"
                measurement = []
                sequence = Sequence(input_string, measurement, time, response)
                self.sequence_history.save_curr_seq(sequence)
                return {"status": "fail", "err_msg": error_message, "result": measurement}

        except Exception as e:
            cherrypy.response.status = 500
            error_message = str(e)
            response = 500
            sequence = Sequence(input_string, measurement=None, time=time, response=response)
            self.sequence_history.save_curr_seq(sequence)
            return {"status": "error", "err_msg": error_message, "result": None}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_history(self):
        """
        Function that exposes an API endpoint to retrieve measurements history
        :return: a JSON response containing the history data, or an error message
        """
        try:
            history = self.sequence_history.get_history()
            return history
        except Exception as e:
            cherrypy.response.status = 500  # Internal Server Error
            return {"status": "error", "err_msg": str(e), "result": None}


