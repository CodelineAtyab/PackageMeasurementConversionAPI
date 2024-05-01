import cherrypy
import logging
from Services.sequence_processor import sequence_compressor
from Models.sequence_history import SequenceHistory

# Configure logging
logging.basicConfig(level=logging.INFO)


class SequenceConverterAPI:
    def __init__(self, db_file):
        # Initialize SequenceHistory with the provided database file
        self.sequence_history = SequenceHistory(db_file)

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def convert_measurements(self, input):
        # Log the received request
        logging.info(f"Received request to convert measurements: {input}")

        # Call sequence_compressor to process the input and get compressed values
        compressed_values = sequence_compressor(input)

        # Save the sequence and its compressed values to the database
        self.sequence_history.save_sequence({'input': input, 'compressed_values': compressed_values})

        # Log the successful conversion
        logging.info(f"Conversion successful: {compressed_values}")

        # Return the compressed values in JSON format
        return compressed_values

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_history(self):
        # Log the request to retrieve history
        logging.info("Retrieving history of sequences")

        # Get the history of sequences from the database
        return self.sequence_history.get_history()
