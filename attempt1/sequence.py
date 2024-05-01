import logging


class Sequence:
    def __init__(self):
        self.sequence = ""
        logging.debug("Sequence initialized as empty.")

    def set_sequence(self, sequence):
        self.sequence = sequence
        logging.debug(f"Sequence set to: {sequence}")

    def encoder(self, character):
        encoder = {
            "_": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8,
            "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17,
            "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
        }
        return encoder[character]

    def is_valid(self):
        sequence = self.sequence

        steps = 0
        index = 0
        is_counting = False
        while index < len(sequence):
            if is_counting:  # IF in the middle of cycle
                steps = steps - 1
                if sequence[index] == 'z':
                    steps = steps + 1
                if steps == 0:
                    is_counting = False
            else:  # IF at the start of cycle
                steps = self.encoder(sequence[index])
                if sequence[index] == 'z':
                    steps = steps + self.encoder(sequence[index + 1])
                    if sequence[index + 1] == 'z':
                        steps = steps + self.encoder(sequence[index + 2])
                        index += 1
                    index += 1
                is_counting = True

            index += 1

        if steps == 0:
            return True
        else:
            return False

    def get_sequence_as_str(self):
        logging.debug(f"Returning sequence: {self.sequence}")
        return self.sequence

    def parse_sequence(self):
        logging.info(f"Parsing sequence: {self.sequence}")

        # Mapping from characters to their respective values
        value_map = {chr(i): i - 96 for i in range(ord('a'), ord('z') + 1)}
        value_map['_'] = 0

        result = []
        current_sum = 0
        current_count = 0

        i = 0
        while i < len(self.sequence):
            if self.sequence[i] == 'z' and i + 1 < len(self.sequence) and self.sequence[i + 1].isalpha():
                # Special handling for 'z' followed by another character
                current_sum += value_map['z']
                i += 1
                while i < len(self.sequence) and self.sequence[i] == 'z':
                    current_sum += value_map['z']
                    i += 1
                if i < len(self.sequence) and self.sequence[i] != '_':
                    current_sum += value_map[self.sequence[i]]
                result.append(current_sum)
                current_sum = 0
                i += 1
            elif self.sequence[i].isalpha():
                current_count = value_map[self.sequence[i]]
                current_sum = 0
                i += 1
                while current_count > 0 and i < len(self.sequence) and self.sequence[i] != '_':
                    current_sum += value_map[self.sequence[i]]
                    current_count -= 1
                    i += 1
                result.append(current_sum)
            else:
                result.append(0)
                i += 1

        logging.info(f"Sequence parsed. Result: {result}")
        return result
