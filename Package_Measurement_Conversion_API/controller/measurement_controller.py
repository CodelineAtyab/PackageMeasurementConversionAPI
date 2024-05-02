import cherrypy
import logging

from Package_Measurement_Conversion_API.services.converter import Measurements
from Package_Measurement_Conversion_API.Utilities.db import MeasurementsDB

# Initialize database manager and measurement conversion service
db_manager = MeasurementsDB("conversion_history.db")
Measure = Measurements()

# Configure logging
logging.basicConfig(filename='Package_Measurement_Conversion_API\logging\error_log.log',
                    level=logging.CRITICAL, format='%(asctime)s:%(levelname)s:%(message)s')


class MeasurementService(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_data_from_db(self):
        """Fetch conversion history from the database."""
        try:
            table = db_manager.display_table()
            return {"status": "success", "err_msg": "", "result": table}
        except Exception as e:
            logging.error(f"Failed to retrieve data: {str(e)}")
            return {"status": "fail", "err_msg": str(e), "result": []}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def convert_measurements(self, input_string):
        """Convert input string to numbers based on specific logic."""
        try:
            if not isinstance(input_string, str):
                raise ValueError("Input must be a string.")

            converted_data = Measure.convert_measurements(input_string)
            if not converted_data:
                raise ValueError("Conversion resulted in empty data.")
            return {"status": "success", "err_msg": "", "result": converted_data}
        except Exception as e:
            logging.exception("Error in convert_measurements:")
            return {"status": "fail", "err_msg": str(e), "result": []}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def conversion_results(self, input_string):
        """Process converted data to compute final results and save them to the database."""
        try:
            results = Measure.measurement_results(input_string)
            db_manager.save_table(input_string, results)  # Assuming the function name is save_conversion
            return {"status": "success", "err_msg": "", "result": results}
        except Exception as e:
            logging.error(f"Failed to process conversion results: {str(e)}")
            return {"status": "fail", "err_msg": str(e), "result": []}

