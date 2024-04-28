import cherrypy
import logging
import argparse

from src.controllers.SequenceController import SequenceRecordsV1

def parse_command_line():
    parser = argparse.ArgumentParser(description="CherryPy Server Configuration")
    parser.add_argument('port', nargs='?', type=int, default=8080, help='Port on which the server will run')
    return parser.parse_args()

if __name__ == '__main__':
    # Parse command line arguments
    args = parse_command_line()

    # Configure LOGGING to file 
    logging.basicConfig(filename='error_log.log', level=logging.CRITICAL, 
                        format='%(asctime)s:%(levelname)s:%(message)s')


    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': args.port})
    cherrypy.tree.mount(SequenceRecordsV1(), '/')


    # Start the CherryPy server
    cherrypy.engine.start()
    cherrypy.engine.block()
