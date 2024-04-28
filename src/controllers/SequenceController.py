import cherrypy

from ..services.SequenceService import SequenceService


class SequenceRecordsV1():
    exposed = True
    
    def __init__(self):
        self.sequence_service = SequenceService()

    @cherrypy.tools.json_out()
    def GET(self, input: str = ""):
        """
        Handles the GET request and return a JSON response.
        """

        # Special Case
        if input[0] == "_":
            res_msg = {"status": "success", "err_msg": "", "result": [0]}
        else:
            self.sequence_service.get_sequence(input)
            res_msg = {"status": "success", "err_msg": "", "result": self.sequence_service.process_sequence()}

        # try:
        #     self.sequence_service.get_sequence(input)
        #     res_msg = {"status": "success", "err_msg": "", "result": self.sequence_service.process_sequence()}
        # except:
        #     res_msg = {"status": "fail", "err_msg": "invalid sequence", "result": []}


        return res_msg
