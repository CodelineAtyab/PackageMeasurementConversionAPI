import cherrypy
import traceback
import json
import os

from src.models.string import String
from src.services.sequence_service import SequenceService
from src.services.sequence_history import FileHandler
from src.models.sequence import StringProcessor


class SequenceAPI(object):
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, input_string: str = ""):
        res_msg = {"status": "FAIL", "data": []}
        file_handler = FileHandler(storage_format='json')
        sequence = SequenceService()
        try:
            if input_string:
                string_instance = String(input_string)
                processor = StringProcessor(string_instance)
                processed_results = processor.create_result()

                res_msg = {"status": "SUCCESS", "data": processed_results}
                sequence.process_and_store_string(input_string)

            else:
                file_data = file_handler.open_write_file(state='r')
                res_msg = {"status": "SUCCESS", "data": file_data}
        except Exception as e:
            print(traceback.format_exc(e))
            res_msg = {"status": "fail", "err_msg": "invalid sequence", "result": []}
            #res_msg["data"] = str(e)

        return res_msg



