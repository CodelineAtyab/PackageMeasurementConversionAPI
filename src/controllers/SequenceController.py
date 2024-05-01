import cherrypy

from src.services.SequenceService import SequenceService
from src.services.SequenceHistory import SequenceHistory


class SequenceRecordsV1():
    
    def __init__(self):
        self.sequence_service = SequenceService()
        self.sequence_history = SequenceHistory()

    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def convert_measurements(self, input: str = ""):
        """
        Handles the GET request and return a JSON response. The API will convert measurement input
        string from a sequence of characters into a result list of the total values of measured 
        inflows for each package.
        """

        try:  
            self.sequence_service.get_sequence(input)
            res_msg = {"status": "success", "err_msg": "", "result": self.sequence_service.process_sequence()}
            self.sequence_history.insert_data("SUCCESS", input)
        except: # If Invalid Sequence
            res_msg = {"status": "fail", "err_msg": "invalid sequence", "result": []}
            self.sequence_history.insert_data("FAILED", input)


        return res_msg
    
    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def get_history(self):
        """
        Handles the GET all records from Database and returns a JSON response.
        """

        res_msg = {"status": "success", "err_msg": "", "result": self.sequence_history.fetch_data()}

        return res_msg
