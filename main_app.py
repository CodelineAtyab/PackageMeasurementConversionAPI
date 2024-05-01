# main_app.py
import cherrypy
from Controllers.sequence_measuremnet_conversion_api import SequenceConverterAPI
import argparse

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Package Measurement Conversion API')
    parser.add_argument('--port', type=int, default=8080, help='Port number to run the server on')
    args = parser.parse_args()

    # Path to SQLite database file
    db_file = 'Utillities/sequence_history.db'

    # Update CherryPy configuration with host and port
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': args.port})

    # Start the CherryPy server with the SequenceConverterAPI instance
    cherrypy.quickstart(SequenceConverterAPI(db_file))
