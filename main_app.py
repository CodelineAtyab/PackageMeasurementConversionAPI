import cherrypy
import os
import sys

from src.controller.sequence_controller import SequenceAPI

class Root(object):
    @cherrypy.expose
    def index(self):
        """
        This function is going to return index.html files present in the static directory.
        We don't need to implement it since it is configured and cherrypy is going to handle it.
        """
        pass

def setup_server(port=8080):
    # Set up logging
    log_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cherrypy.log')
    cherrypy.log.error_file = log_file
    cherrypy.log.access_file = log_file

    # Configure the global settings for CherryPy
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': port,
        'log.error_file': log_file,
        'log.screen': True,
        'log.access_file': log_file
    })

    # Mount the ContactsAPI application
    cherrypy.tree.mount(SequenceAPI(), '/api/sequence', {
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

if __name__ == "__main__":
    # Default port is 8080 unless specified
    port = 8080
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 8080.")

    setup_server(port)
