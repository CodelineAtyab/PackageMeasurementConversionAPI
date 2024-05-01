from src.models.sequence import Sequence
from src.services.sequence_processor import SequenceProcessor
from src.utils.File_Handler import FileHandler


class SequenceService:
    def __init__(self, storage_format):
        self.file_handler = FileHandler(storage_format=storage_format)

    def input_service(self, input_string):
        """
        Takes an input string, processes it using StringProcessor, and stores the results.
        """
        # Process the string using StringProcessor
        sequence = Sequence(input_string)
        processor = SequenceProcessor(sequence)
        processed_results = processor.create_result()

        # Convert results to the desired format (JSON, CSV, TXT)
        formatted_data = self.file_handler.dataformat.format(sequence)

        # Store the formatted data
        self.file_handler.open_write_file(data=formatted_data, state="a")
        return processed_results, formatted_data


# Example usage
if __name__ == "__main__":
    sequence_service = SequenceService(storage_format='db')
    test_string = 'dz_a_aazzaaa'
    results, formatted = sequence_service.input_service(test_string)
    print(f"Processed Results: {results}, Formatted and Stored: {formatted}")
