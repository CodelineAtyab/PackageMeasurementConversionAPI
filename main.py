import cherrypy
import logging

from controller.measurement_controller import MeasurementAPI


if __name__ == '__main__':
    logging.basicConfig(filename='error_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})

    cherrypy.quickstart(MeasurementAPI(), '/')
