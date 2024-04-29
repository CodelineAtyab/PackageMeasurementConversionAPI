import cherrypy
from controller.measurement_converter_api import MeasurementConverterAPI


if __name__ == '__main__':
    cherrypy.tree.mount(MeasurementConverterAPI(), '/')
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()