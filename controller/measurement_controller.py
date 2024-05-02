import cherrypy
import sqlite3
from services.measurement_service import convert_measurements  # Ensure this module and function are correctly implemented.
import logging
from db_utils.db_crud_operations import DbCrudOpearations
from models.processed_result import ProcessResult
import ast

#DATABASE_NAME = "measurements.db"

class MeasurementAPI:
    def __init__(self) -> None:
        self.storing_history = DbCrudOpearations()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def convert(self, input_str=""):
        if not input_str:
            return {"status": "fail", "err_msg": "invalid sequence", "result": []}
        result = convert_measurements(input_str)
        # Create a new object and then pass it
        # self.add_to_history(input_str, str(result))
        processed_result_obj=ProcessResult()
        processed_result_obj.given_seq = input_str
        processed_result_obj.generated_seq = str(result)
        
        self.storing_history.add_to_history(processed_result_obj)
        return {"status": "success", "err_msg": "", "result": ast.literal_eval(processed_result_obj.generated_seq)}  #To convert a string representation of a list into an actual list in Python, you can use the ast.literal_eval() function from the ast module. this is done for easier testing as tester wants it in a certain format
        #return {"input": processed_result_obj.given_seq, "output": processed_result_obj.generated_seq}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def history(self):
        return {"history": self.storing_history.get_history()}
    