import time
from datetime import datetime


class Sequence:
    def __init__(self, input_string, created_at_epoch_time=time.time()):
        self.input_string = input_string
        self.created_at = created_at_epoch_time

    def get_string(self):
        return self.input_string

    def to_dict(self):
        """Convert the Sequence object attributes to a dictionary for easy JSON serialization."""
        return {
            'input_string': self.input_string,
            'created_at': self.created_at
        }
