import cherrypy
import logging
from sequenceservice import SequenceService

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class PackageMeasurementAPI:
    def __init__(self):
        self.service = SequenceService()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def convert_measurements(self, input_sequence=None):
        if input_sequence is None:
            logging.info("No input provided, fetching history.")
            try:
                history = self.service.get_history()
                return {"history": history}
            except Exception as e:
                logging.error("Error fetching history", exc_info=True)
                cherrypy.response.status = 500
                return {"error": str(e)}
        else:
            logging.info(f"Received input for conversion: {input_sequence}")
            try:
                result = self.service.process_sequence(input_sequence)
                logging.info(f"Conversion result for '{input_sequence}': {result}")
                return {"input": input_sequence, "result": result}
            except Exception as e:
                logging.error("Error processing conversion", exc_info=True)
                cherrypy.response.status = 400
                return {"error": str(e)}


if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080
    })
    logging.info("Starting web server...")
    cherrypy.quickstart(PackageMeasurementAPI(), '/')
