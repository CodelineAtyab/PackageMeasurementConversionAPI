from src.serializers.JSONdataformat import JSONDataFormat
from src.models.sequence import Sequence
from src.serializers.SQLDataFormat import SQLDataFormat


class FileHandler:
    BASE_FILE_PATH = "./src/data/store_sequence"

    def __init__(self, storage_format):
        self.set_datastore(storage_format)
        self.storage_format = storage_format
        self.dataformat = self.set_datastore(storage_format)
        self.INPUT_FILE_PATH = f"{self.BASE_FILE_PATH}.{storage_format}"

    def format_record(self, input_string):
        """
        :param input_string: input_string
        :return: chooses the format of file based on user input
        """
        inputstring = Sequence(input_string)
        return self.dataformat.format(inputstring)

    def set_datastore(self, storage_format):
        """

        :param storage_format: changes format type based on what's written in the
        controller.
        :return: If it's db, then the db format is chosen, if JSON, the JSON format is chosen.
        """
        if storage_format == 'db':
            return SQLDataFormat()
        elif storage_format == 'json':
            return JSONDataFormat()
        self.INPUT_FILE_PATH = f"{self.BASE_FILE_PATH}.{storage_format}"

    def open_write_file(self, data="", state="r"):
        """
        contains all file related functions such as, Write, Read, Append to main file
        :param data: user inputted record
        :param state: a, r, or w
        :return: Data Saved Successfully!
        """
        with open(self.INPUT_FILE_PATH, state) as input_file:
            if state in ["a", "w"]:
                input_file.write(data)
            elif state == "r":
                return [x.strip() for x in input_file.readlines()]
