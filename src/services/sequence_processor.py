from src.models.sequence import Sequence


class SequenceProcessor:
    def __init__(self, string_instance: Sequence):
        self.input_string = string_instance.get_string()
        self.results = []
        self.converted_list = []
        self.combined_list = []

    def process_string_to_list(self):
        """
        Convert the input string to a list of integers based on character positions,
        where 'a' is 1, 'z' is 26, and '_' is 0.
        """
        for char in self.input_string:
            if 'a' <= char <= 'z':
                num_chars_to_consider = ord(char) - ord('a') + 1
                self.append_converted_list(num_chars_to_consider)
            elif char == '_':
                self.append_converted_list(0)

    def append_converted_list(self, value):
        """
        :param value: Is the converted chars to position nums from Process_string_to_list func
        :return: appends value to converted list.
        """
        self.converted_list.append(value)
        return self.converted_list

    def append_combined_list(self, num):
        """

        :param num: contains list processed by handle z_case func.
        :return: appends new list to combined_list
        """
        self.combined_list.append(num)
        return self.combined_list

    def append_result(self, seq):
        """

        :param seq: contains value of each sequence.
        :return: appends sequence to result.
        """
        self.results.append(seq)
        return self.results

    def handle_z_case(self):
        """
        Combine all consecutive 26s in the list with the next non-26 value.
        In order to handle Z cases as intended.
        """
        i = 0
        while i < len(self.converted_list):
            if self.converted_list[i] == 26:
                sum_26 = 0
                while i < len(self.converted_list) and self.converted_list[i] == 26:
                    sum_26 += self.converted_list[i]
                    i += 1
                if i < len(self.converted_list):
                    sum_26 += self.converted_list[i]
                self.append_combined_list(sum_26)
                i += 1
            else:
                self.append_combined_list(self.converted_list[i])
                i += 1
        return self.combined_list

    def create_result(self):
        """
        Process the input string to combine consecutive 26s with the next value,
         and calculate sums.
        """
        if self.input_string.startswith('_'):
            return [0]

        self.results = []
        converted_list = self.process_string_to_list()
        combined_list = self.handle_z_case()
        i = 0

        while i < len(combined_list):
            count = combined_list[i] if i < len(combined_list) else 0
            sum_sequence = 0
            if count > 0 and i + 1 < len(combined_list):
                sum_sequence = sum(combined_list[i + 1:i + 1 + count])
            self.append_result(sum_sequence)
            i += count + 1

            if i >= len(combined_list) and (count == 0 or i + 1 >= len(combined_list)):
                break

        return self.results


# Example usage
if __name__ == "__main__":
    test_strings = [
        'abbcc', 'dz_a_aazzaaa', 'a_', 'abcdabcdab', 'abcdabcdab_',
        'zdaaaaaaaabaaaaaaaabaaaaaaaabbaa',
        'zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_',
        'za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa', '_a', '_', '_ad', '_zzzb', '__'
    ]

    for test_string in test_strings:
        processor = SequenceProcessor(test_string)
        result = processor.create_result()
        print(f"Input: {test_string} -> Got: {result}")
