import time
from datetime import datetime


class String:
    def __init__(self, input_string):
        self.input_string = input_string

    def get_string(self):
        return self.input_string

    def epoch_time(self):
        stamp = time.time()  # Get current epoch time in seconds
        # Convert epoch time to a datetime object and format it
        date_time = datetime.fromtimestamp(stamp).strftime('%Y-%m-%d %H:%M:%S')

        return date_time
