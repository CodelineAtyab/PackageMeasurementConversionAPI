import json

from src.abstraction.dataformat import DataFormat
from src.models.sequence import Sequence


class JSONDataFormat(DataFormat):
    def format(self, input_string: Sequence):
        """
        Formats input data with created time into JSON format.
        :param input_string: contains the sequence the user inputted
        :return: formatted in JSON data to be saved to JSON file
        """
        return json.dumps({
            "input_string": input_string.get_string(),
            "input_time": input_string.created_at
        }) + "\n"

