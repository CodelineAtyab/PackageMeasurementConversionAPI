import cherrypy
import logging
from controller.measurement_converter_api import MeasurementConverterAPI


if __name__ == '__main__':
    # Configure logging
    logging.basicConfig(filename='./logs/measurement_log.log', level=logging.CRITICAL,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    
    cherrypy.tree.mount(MeasurementConverterAPI(), '/')
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()