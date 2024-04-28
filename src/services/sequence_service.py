from src.models.string import String
from src.models.sequence import StringProcessor
from src.services.sequence_history import FileHandler


class SequenceService:
    def __init__(self, storage_format='json'):
        self.file_handler = FileHandler(storage_format=storage_format)

    def process_and_store_string(self, input_string):
        """
        Takes an input string, processes it using StringProcessor, and stores the results.
        """
        # Process the string using StringProcessor
        string = String(input_string)
        processor = StringProcessor(string)
        processed_results = processor.create_result()

        # Convert results to the desired format (JSON, CSV, TXT)
        formatted_data = self.file_handler.dataformat.format(input_string)

        # Store the formatted data
        self.file_handler.open_write_file(data=formatted_data, state="a")
        return processed_results, formatted_data


# Example usage
if __name__ == "__main__":
    sequence_service = SequenceService(storage_format='json')
    test_string = 'dz_a_aazzaaa'
    results, formatted = sequence_service.process_and_store_string(test_string)
    print(f"Processed Results: {results}, Formatted and Stored: {formatted}")
