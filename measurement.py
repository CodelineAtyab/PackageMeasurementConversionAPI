import cherrypy
import logging
from converter import Measurements
from database import Database

# Setup for logging
logging.basicConfig(
    filename='logs/conversion_errors.log',  # Simplified path
    level=logging.DEBUG,  # Adjusted log level for more verbose output during development
    format='%(asctime)s:%(levelname)s:%(message)s'
)

# Database manager instance
db_manager = Database("conversion_history.db")
measure = Measurements()  # Instance of the Measurements class

class MeasurementService:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_conversion_history(self):
        """Endpoint to fetch the conversion history from the database."""
        try:
            history_data = db_manager.fetch_conversion_history()
            return {"status": "success", "data": history_data}
        except Exception as e:
            logging.error("Failed to retrieve history: {}".format(str(e)))
            return {"status": "error", "message": str(e)}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def convert_input(self, input_string=""):
        """Endpoint to convert alphabetic inputs into their corresponding numeric values."""
        if input_string:
            try:
                result = measure.convert_measurements(input_string)
                db_manager.record_conversion(input_string, result)
                return {"input": input_string, "output": result, "status": "success"}
            except ValueError as e:
                logging.warning(f"Validation error: {e}")
                return {"status": "error", "message": str(e)}
            except Exception as e:
                logging.critical("Unexpected error in conversion: {}".format(str(e)), exc_info=True)
                return {"status": "error", "message": "An unexpected error occurred"}
        else:
            return {"status": "error", "message": "No input provided"}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_measurement_results(self, input_string):
        """Endpoint to calculate results based on converted measurements."""
        try:
            results = measure.measurement_results(input_string)
            db_manager.save_results(input_string, results)
            return {"input": input_string, "results": results, "status": "success"}
        except Exception as e:
            logging.error("Error processing results: {}".format(str(e)))
            return {"status": "error", "message": str(e)}