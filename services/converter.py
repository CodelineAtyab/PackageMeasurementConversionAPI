import string


class PackageConverter:
    def convert_measurements(self, input_string: str) -> list:
        """Convert input string to a list of summed measurements."""
        values = [self.convert_char_to_value(char) for char in input_string]
        lst = self.convert(values)
        return self.process_measurements(lst)

    @staticmethod
    def convert_char_to_value(char: str) -> int:
        """Convert a character to its corresponding numeric value."""
        if char == '_':
            return 0
        return string.ascii_lowercase.index(char.lower()) + 1
    def is_empty(self, lst):
        if len(lst) < 1:
            return True
        else:
            return False

    def convert(self, lst):
        count = 0
        i = 0
        while not self.is_empty(lst):
            # print(lst[i])
            if i >= len(lst):
                if count >= 26:
                    return "invalid"
                return lst
            elif lst[i] >= 26:
                count += 26
                lst.pop(i)

            else:
                count += lst[i]
                lst[i] = count
                i += 1
                count = 0
        return lst




    def process_measurements(self, values: list) -> list:
        """Process list of numeric values and sum according to the encoded rules."""
        result = []
        i = 0
        # for i in range(len(values)):
        if values != "invalid":

            while not self.is_empty(values):
                length = values[0]
                values.pop(0)
                # print(length, ": ", len(values))
                if length == 0:  #or i + length >= len(values):
                    result.append(0)
                    break
                elif length > len(values):
                    result = []
                    break

                else:
                    # result.append(sum(values[i+1:i+1+length]))
                    result.append(sum(values[:length]))
                    values = values[length:]
                    # i += length + 1
        else:
            result = []
        return result


converter = PackageConverter()
# print(converter.convert_measurements("aaa"))
print(converter.convert_measurements("abz"))
# print(converter.convert_measurements("abc"))