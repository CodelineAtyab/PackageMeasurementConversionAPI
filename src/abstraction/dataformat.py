"""
DataFormat is an abstract class that has three subclasses, which minuplate the data into the chosen format,
such as, TXT, JSON, CSV
"""

from abc import ABC, abstractmethod


class DataFormat(ABC):
    def __init__(self):
        self.data_formatter = None

    @abstractmethod
    def format(self, input_string):
        pass
