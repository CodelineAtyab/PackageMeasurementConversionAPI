import cherrypy
import os


from src.controllers.SequenceController import SequenceRecordsV1


class Root(object):
    @cherrypy.expose()
    def index(self):
        """
        This function is going to return index.html files present in the static directory.
        We don't need to implement it since it configured and cherrypy is going to handle it.
        """
        pass


cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8888})

# Mount the application
cherrypy.tree.mount(SequenceRecordsV1(), '/convert-measurements', {
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),  # Use method-based dispatching
        'tools.sessions.on': False,
        'tools.response_headers.on': True,
        'tools.response_headers.headers': [('Content-Type', 'text/plain')]
    }
})

cherrypy.tree.mount(Root(), '/', {
    '/': {
            'tools.staticdir.root': os.path.abspath(os.path.dirname(__file__)),
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'static',
            'tools.staticdir.index': 'index.html',
    }
})

# Start the CherryPy server
cherrypy.engine.start()
cherrypy.engine.block()
