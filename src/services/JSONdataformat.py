import json

from src.services.dataformat import DataFormat
from src.models.string import String


class JSONDataFormat(DataFormat):
    def format(self, input_string):
        return json.dumps({
            "input_string": input_string,
            "input_time": String.epoch_time(self)
        }) + "\n"

