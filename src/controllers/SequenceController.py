import cherrypy

from src.services.SequenceService import SequenceService


service = SequenceService()

class SequenceRecordsV1():
    exposed = True
    

    @cherrypy.tools.json_out()
    def GET(self, input: str = ""):
        """
        Handles the GET request and return a JSON response.
        """

        try:
            service.get_sequence(input)
            res_msg = {"status": "success", "err_msg": "", "result": service.process_sequence()}
        except:
            res_msg = {"status": "fail", "err_msg": "invalid sequence", "result": []}


        return res_msg
