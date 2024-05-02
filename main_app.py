import cherrypy

from Package_Measurement_Conversion_API.controller.measurement_controller import MeasurementService


if __name__ == '__main__':
    config = {
        '/': {
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    cherrypy.config.update({'server.socket_host': "0.0.0.0"})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.quickstart(MeasurementService(), '/', config)
