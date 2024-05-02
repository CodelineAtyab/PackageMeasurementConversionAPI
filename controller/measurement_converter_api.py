import cherrypy
import json
from services.measurement_converter import MeasurementConverter
from utils.measurement_converter_db import MeasurementConverterDB
from models.measurement_history import MeasurementHistory

class MeasurementConverterAPI(object):
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def convert_measurements(self, input_str=None):
        """
        Convert the measurements to the sum of letter values for each segment.
        """
        db_entry = MeasurementHistory
        db_entry.input = input_str
        try:
            if input_str is None:
                raise cherrypy.HTTPError(400, "Missing input parameter")
            db_entry.output = MeasurementConverter().package_measurement_converter(input_str)
            MeasurementConverterDB().save_to_history(db_entry.input, db_entry.output)
            error_msg = "Invalid string input" if db_entry.output == "Invalid string input" else ""
            status = "SUCCESS" if error_msg == "" else "FAIL"
            result = db_entry.output if error_msg == "" else []
            return {"status": status, "error_msg": error_msg, "result": result}
        except Exception as e:
            return {"status": "FAIL", "error_msg": str(e), "result": []}
            
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_history(self):
        """
        Get the history of the measurements from the database.
        """
        try:
            db_instance = MeasurementConverterDB() 
        except:
            raise cherrypy.HTTPError(500, "Database connection error")
        
        return db_instance.get_history()

