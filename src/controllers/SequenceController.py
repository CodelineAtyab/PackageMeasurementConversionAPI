import cherrypy

from ..services.SequenceService import SequenceService
from ..services.SequenceHistory import SequenceHistory


class SequenceRecordsV1():
    
    def __init__(self):
        self.sequence_service = SequenceService()
        self.sequence_history = SequenceHistory()

    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def convert_measurements(self, input: str = ""):
        """
        Handles the GET request and return a JSON response.
        """

        # Special Case
        if input[0] == "_":
            res_msg = {"status": "success", "err_msg": "", "result": [0]}

            self.sequence_history.insert_data(input)
            self.sequence_history.close()
        else:
            
            self.sequence_service.get_sequence(input)
            res_msg = {"status": "success", "err_msg": "", "result": self.sequence_service.process_sequence()}

            self.sequence_history.insert_data(input)
            self.sequence_history.close()

        # try:
        #     self.sequence_service.get_sequence(input)
        #     res_msg = {"status": "success", "err_msg": "", "result": self.sequence_service.process_sequence()}
        # except:
        #     res_msg = {"status": "fail", "err_msg": "invalid sequence", "result": []}

        return res_msg
    
    @cherrypy.expose()
    @cherrypy.tools.json_out()
    def get_all(self):
        """
        Handles the GET all records from Database and returns a JSON response.
        """

        res_msg = {"status": "success", "err_msg": "", "result": self.sequence_history.fetch_data()}
        self.sequence_history.close()

        return res_msg
