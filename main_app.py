import cherrypy
import sys
import logging

from controller.handlers import MeasurementConversionHandler

if __name__ == '__main__':
    port = 8080    # Default port

    # Check if a custom port is provided as an argument
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using the default port (8080).")

    # Configure LOGGING to file
    logging.basicConfig(filename='error_logs.log', level=logging.CRITICAL,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    # Mount the MeasurementConversionHandler to the CherryPy root
    cherrypy.tree.mount(MeasurementConversionHandler(), '/')
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': port})

    # Start the CherryPy server
    cherrypy.engine.start()
    cherrypy.engine.block()


