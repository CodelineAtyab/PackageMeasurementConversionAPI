import sys
import logging
import cherrypy
from controller.controller import ConverterAPI


def setup_logging():
    logging.basicConfig(
        filename='utilities/error_log.log',
        level=logging.CRITICAL,
        format='%(asctime)s:%(levelname)s:%(message)s'
    )
    logging.getLogger().addHandler(logging.StreamHandler())


def start_server(port=8080):
    try:
        cherrypy.config.update({
            'server.socket_host': '0.0.0.0',
            'server.socket_port': port
        })
        cherrypy.tree.mount(ConverterAPI(), '/')
        cherrypy.engine.start()
        cherrypy.engine.block()
    except Exception as e:
        logging.critical("Failed to start server: ", exc_info=e)


if __name__ == '__main__':
    setup_logging()
    port = 8080  # Default port
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            logging.error("Invalid port number provided. Using default port (8080).")

    start_server(port)
