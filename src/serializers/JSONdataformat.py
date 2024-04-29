import json

from src.abstraction.dataformat import DataFormat
from src.models.sequence import Sequence


class JSONDataFormat(DataFormat):
    def format(self, input_string: Sequence):
        return json.dumps({
            "input_string": input_string.get_string(),
            "input_time": input_string.created_at
        }) + "\n"

