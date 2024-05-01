from src.models.Sequence import Sequence
from src.services.SequenceHistory import SequenceHistory


class SequenceService:

    def __init__(self):
        self.sequence_manager = Sequence()
        self.sequence_history = SequenceHistory()
        self.result = []

    # Receives the input sequenece from the API endpoint and stores it as a Sequence object.
    def get_sequence(self, str_representation):
        self.sequence_manager.set_sequence(str_representation)
    
    # Adds integer to result list (sum of each cycle) and returns it.
    def append_num_to_list(self, number):
        self.result.append(number)
        return self.result

    # Processes the Sequence object and returns the result list.
    def process_sequence(self):
        sequence = self.sequence_manager.get_sequence_as_str()

        # Check if input is valid
        if sequence[0] == "_": # Special Case for "_"
            return [0]
        elif self.sequence_manager.is_valid():
            pass
        else:
            raise Exception("INVALID SEQUENCE")
        
        self.result = []
        index = 0
        is_counting = False
        while index < len(sequence):
            if is_counting:
                if steps != 0:
                    if sequence[index] == 'z':
                        sum = sum + self.sequence_manager.encoder(sequence[index])
                    else:         
                        sum = sum + self.sequence_manager.encoder(sequence[index])
                        steps -= 1
                        if (index + 1) == len(sequence):
                            self.append_num_to_list(sum)
                else:
                    if steps == 0:
                        index -= 1
                    self.append_num_to_list(sum)
                    is_counting = False
            else:
                sum = 0
                steps = self.sequence_manager.encoder(sequence[index])

                if steps == 0 and index + 1 == len(sequence):
                    self.append_num_to_list(sum)
                else:
                    if sequence[index] == 'z':
                        steps = steps + self.sequence_manager.encoder(sequence[index + 1])
                        if sequence[index + 1] == 'z':
                            steps = steps + self.sequence_manager.encoder(sequence[index + 2])
                            index += 1
                        index += 1
                    is_counting = True
            index += 1

        return self.result