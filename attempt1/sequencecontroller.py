import cherrypy
from sequenceservice import SequenceService


class SequenceController:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, input_str=''):
        service = SequenceService()
        result = service.process_sequence(input_str)
        return result
