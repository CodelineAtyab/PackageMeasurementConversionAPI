import json
import os
import time

from src.services.JSONdataformat import JSONDataFormat
from src.services.dataformat import DataFormat
from src.models.string import String
from src.services.SQLDataFormat import SQLDataFormat


class FileHandler:
    BASE_FILE_PATH = "./src/data/store_sequence"

    def __init__(self, storage_format):
        self.set_datastore(storage_format)
        self.storage_format = storage_format
        self.dataformat: DataFormat = JSONDataFormat()
        self.INPUT_FILE_PATH = f"{self.BASE_FILE_PATH}.{storage_format}"

    def format_record(self, input_string):
        """
        :param input_string: input_string
        :return: chooses the format of file based on user input
        """
        inputstring = String(input_string)
        return self.dataformat.format(inputstring)

    def set_datastore(self, storage_format):
        if storage_format == 'sql':
            self.dataformat = SQLDataFormat()
        # elif storage_format == 'txt':
        #     self.dataformat = TXTDataFormat()
        elif storage_format == 'json':
            self.dataformat = JSONDataFormat()
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

    def read_contact(self, search):
        """
        Search for a specific record based on unique key, in this case the name.
        e.g: input: John Doe
             output: Name: John Doe, Phone Number: 1234, Email: John@gmail.com, Address: Oman
        """
        try:
            inputs = self.open_write_file()
            for strings in inputs:
                string_details = strings.split(",")

                if string_details[1].strip().lower() == search.strip().lower():
                    return f"[input_string: {string_details[0]}, Time {string_details[1]}]"
            return "Not found"
        except Exception as ex:
            print("Error", ex)

