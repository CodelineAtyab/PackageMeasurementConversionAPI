import string


class PackageConverter:
    def convert_measurements(self, input_string: str) -> list:
        """Convert input string to a list of summed measurements."""
        values = [self.convert_char_to_value(char) for char in input_string]
        return self.process_measurements(values)

    @staticmethod
    def convert_char_to_value(char: str) -> int:
        """Convert a character to its corresponding numeric value."""
        if char == '_':
            return 0
        return string.ascii_lowercase.index(char.lower()) + 1

    def process_measurements(self, values: list) -> list:
        """Process list of numeric values and sum according to the encoded rules."""
        result = []
        i = 0
        while i < len(values):
            length = values[i]
            if length == 0 or i + length >= len(values):
                result.append(0)
                break
            result.append(sum(values[i+1:i+1+length]))
            i += length + 1
        return result
