from sequence import Sequence
from sequencehistory import SequenceHistory


class SequenceService:
    def __init__(self):
        self.sequence_manager = Sequence()
        self.sequence_history = SequenceHistory()
        self.result = []

    def get_sequence(self, str_representation):
        self.sequence_manager.set_sequence(str_representation)
        if not self.sequence_manager.is_valid():
            raise Exception("INVALID SEQUENCE")

    def append_num_to_list(self, number):
        self.result.append(number)
        return self.result

    def process_sequence(self):
        sequence = self.sequence_manager.get_sequence_as_str()
        self.result = []
        index = 0
        is_counting = False
        sum = 0
        steps = 0

        while index < len(sequence):
            current_char = sequence[index]
            current_value = self.sequence_manager.encoder(current_char)
            if current_value == 26:  # 'z'
                sum = 26
                index += 1
                while index < len(sequence) and self.sequence_manager.encoder(sequence[index]) == 26:
                    sum += 26
                    index += 1
                if index < len(sequence) and self.sequence_manager.encoder(sequence[index]) != 0:
                    sum += self.sequence_manager.encoder(sequence[index])
                    index += 1

                count = sum
                sum = 0
                while count > 0 and index < len(sequence):
                    sum += self.sequence_manager.encoder(sequence[index])
                    count -= 1
                    index += 1
                self.append_num_to_list(sum)
            elif 1 <= current_value <= 25 or current_value == 0:
                count = current_value if current_value > 0 else 1
                sum = 0
                index += 1
                while count > 0 and index < len(sequence):
                    sum += self.sequence_manager.encoder(sequence[index])
                    count -= 1
                    index += 1
                self.append_num_to_list(sum)
            index += 1

        # Log the sequence and result to history
        self.sequence_history.add_entry(sequence, self.result)

        return self.result
