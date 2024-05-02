import cherrypy
import traceback

from src.models.sequence import Sequence
from src.services.sequence_service import SequenceService
from src.utils.File_Handler import FileHandler
from src.services.sequence_processor import SequenceProcessor
from src.utils.sequence_history import SequenceHistoryModel


class SequenceAPI(object):
    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, input_string: str = ""):
        res_msg = {"status": "FAIL", "result": []}
        storage_type = "db"
        file_handler = FileHandler(storage_type)
        sequence = SequenceService(storage_type)

        try:
            if input_string:
                string_instance = Sequence(input_string)
                processor = SequenceProcessor(string_instance)
                processed_results = processor.create_result()

                res_msg = {"status": "SUCCESS", "err_msg": "", "result": processed_results}
                sequence.input_service(input_string)

            else:
                sequencehistory = SequenceHistoryModel()
                file_data = [seq.to_dict() for seq in sequencehistory.data]
                res_msg = {"status": "SUCCESS", "err_msg": "", "result": file_data}
        except Exception as e:
            print(traceback.format_exc(e))
            res_msg = {"status": "fail", "err_msg": "invalid sequence", "result": []}

        return res_msg



