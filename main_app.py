import sys
import logging
import cherrypy
from controller.converter_controller import ConverterAPI


if __name__ == '__main__':

    # Configure LOGGING to file
    logging.basicConfig(filename='utilis/error_log.log', level=logging.CRITICAL,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    port = 8080  # Default port

    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using the default port (8080).")

    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': port})
    cherrypy.tree.mount(ConverterAPI(), '/')
    cherrypy.engine.start()
    cherrypy.engine.block()
