import cherrypy
from datetime import datetime

from services.converter import PackageConverter
from utilities.db import PackageMeasurementHistory
from models.sequence import Sequence


class ConverterAPI:
    def __init__(self):
        self.converter = PackageConverter()
        self.sequence_history = PackageMeasurementHistory('./utilities/converter.db')

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
                    "err_msg": "",
                    "result": measurement if measurement != "Invalid" else None}
        except Exception as e:
            cherrypy.response.status = 500
            return {"status": "fail",  "err_msg": str(e), "result": None}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_history(self):
        """
        API endpoint to retrieve measurement history.
        """
        try:
            history = self.sequence_history.get_history()
            return {"status": "success",  "err_msg": "","data": history}
        except Exception as e:
            cherrypy.response.status = 500
            return {"status": "error",  "err_msg": str(e), "data": None}
