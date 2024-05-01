import cherrypy
from datetime import datetime

from services.converter import PackageConverter
from utilities.db import PackageMeasurementHistory
from models.sequence import Sequence

class ConverterAPI:
    def __init__(self):
        self.converter = PackageConverter()
        self.sequence_history = PackageMeasurementHistory('./utilis/converter.db')

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def convert_measurements(self, input=None):
        """
        API endpoint to convert measurements from an input string.
        """
        try:
            input_string = input if input is not None else cherrypy.request.params.get("input", "")
            measurement = self.converter.convert_measurements(input_string)  # Updated method name
            time = datetime.now()
            response = "Measurements processed" if measurement != "Invalid" else "Invalid input"
            sequence = Sequence(input_string, measurement, time, response)
            self.sequence_history.save_curr_seq(sequence)  # Ensure this method accepts a Sequence object

            return {"status": "success" if measurement != "Invalid" else "fail",
                    "data": measurement if measurement != "Invalid" else None,
                    "error": None if measurement != "Invalid" else "Invalid input"}
        except Exception as e:
            cherrypy.response.status = 500
            return {"status": "error", "data": None, "error": str(e)}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_history(self):
        """
        API endpoint to retrieve measurement history.
        """
        try:
            history = self.sequence_history.get_history()
            return {"status": "success", "data": history, "error": None}
        except Exception as e:
            cherrypy.response.status = 500
            return {"status": "error", "data": None, "error": str(e)}
