import cherrypy
from models.package_converter import PackageConverter
from models.sequence_history import SequenceHistory
from models.sequence_history import Sequence


class ConverterAPI:
    def __init__(self):
        self.converter = PackageConverter()
        self.sequence_history = SequenceHistory('converter.db')

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

            if measurement != "Invalid":
                # Assuming no error message or response for now
                error_message = None
                response = "Measurements saved successfully"

                sequence = Sequence(input_string, measurement)
                self.sequence_history.save_curr_seq(sequence, error_message, response)
                return {"status": "success",
                        "response": response, "measurements": measurement,
                        "error": error_message}

            else:
                error_message = "Invalid input"
                response = "cant convert measurement input string"
                measurement = None
                sequence = Sequence(input_string, measurement)
                self.sequence_history.save_curr_seq(sequence, error_message, response)
                return {"status": "error",
                        "response": response, "measurements": measurement,
                        "error": error_message}

        except Exception as e:
            cherrypy.response.status = 500
            error_message = str(e)
            response = 500
            self.sequence_history.save_curr_seq(sequence, error_message, response)
            return {"status": "error", "data": None, "error": str(e)}

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
            return {"status": "error", "data": None, "error": str(e)}

