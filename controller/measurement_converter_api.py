import cherrypy
from models.measurement_converter import MeasurementConverter
from models.measurement_converter_db import MeasurementConverterDB

class MeasurementConverterAPI(object):
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def convert_measurements(self, input_str=None):
        """
        Convert the measurements to the sum of letter values for each segment.
        """
        try:
            if input_str is None:
                    raise cherrypy.HTTPError(400, "Missing input parameter")
            output = MeasurementConverter().pmc(input_str)
            MeasurementConverterDB().save_to_history(input_str, output)
        except Exception as e:
            raise cherrypy.HTTPError(400, str(e))
        
        return output
        
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

