import string


class PackageConverter:
    def __init__(self):
        pass

    def search(self, lst):
        """
        Function to count the number of the letter z
        :param lst: a list containing numbers
        :return: an integer indicating the occurrences of z
        """
        count = 0
        for i in lst:
            if i != 26:
                return count
            elif i == "invalid":
                return "invalid"
            count += 1

    def calc(self, lst):
        """
        Function to return the sum of a given list
        :param lst: a list containing integers
        :return: an integer indicating the sum of a list
        """
        return sum(lst)

    def is_empty(self, lst):
        """
        Function to check if the list is empty
        :param lst: a list of integers
        :return: a boolean (True/False)
        """
        return len(lst) < 1

    def convert_char_to_conversion(self, char):
        """
        Function to convert characters to numeric values
        :param char: a single character either a letter or an underscore
        :return: an integer value of the character
        """
        if char == '_':
            return 0
        elif char.lower() in string.ascii_lowercase:
            return string.ascii_lowercase.index(char.lower()) + 1
        else:
            return "invalid"

    def process_list(self, lst):
        """
        Function to process the list and add values of z (26) together. It also checks if z is the last character
        :param lst: a list containing integers
        :return: returns the processed list, or returns invalid in case z was the last character
        """
        i = 0
        while i < len(lst):

            if lst[i] == 26:
                if i < len(lst) - 1:
                    new_num = self.search(lst[i:])
                    lst[i + new_num] += lst[i] * new_num

                    del lst[i:i + new_num]
                    i += new_num
                    i += 1
                else:
                    return "Invalid"
            elif lst[i] == "invalid":
                return "Invalid"
            else:
                i += 1
        return lst

    def package_measurement_conversion(self, input_string):
        """
        Function to convert a sequence of characters to a list of the total measurements
        :param input_string: a string inputted by the user
        :return: a list of the measurements calculated from the input string
        """
        package_list = [self.convert_char_to_conversion(char) for char in input_string]

        list_to_measure = self.process_list(package_list)
        measurements = []
        if list_to_measure == "Invalid":
            measurements = "Invalid"
        else:
            while not self.is_empty(list_to_measure):
                n = list_to_measure[0]
                if n == 0:
                    measurements.append(0)
                    break
                elif n >= len(list_to_measure) or self.is_empty(list_to_measure):
                    measurements = "Invalid"
                    break
                else:
                    list_to_measure.pop(0)
                    measurements.append(self.calc(list_to_measure[:n]))
                    list_to_measure = list_to_measure[n:]
        return measurements



# # # Test the function
converter = PackageConverter()
print(converter.package_measurement_conversion("@@@")) # [1]
# converter.package_measurement_conversion("__") # [0]
# converter.package_measurement_conversion("a_") # [0]
# converter.package_measurement_conversion("abz") # invalid
# converter.package_measurement_conversion("abc") # invalid
#
# converter.package_measurement_conversion("baaca") # invalid
# converter.package_measurement_conversion("aaa") # invalid
# converter.package_measurement_conversion("bbb") # [4]
# converter.package_measurement_conversion("ccc") # invalid
# converter.package_measurement_conversion('abbcc') # [2,6]
# converter.package_measurement_conversion('abcdabcdab') # [2,7,7]
# converter.package_measurement_conversion('abcdabcdab_') # [[2, 7, 7, 0 ]
# converter.package_measurement_conversion('dz_a_aazzaaa') # [28, 53, 1]
# converter.package_measurement_conversion('zdaaaaaaaabaaaaaaaabaaaaaaaabbaa') # [34]
# converter.package_measurement_conversion('za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa') # [40,1]
# converter.package_measurement_conversion('zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_') # [26]
# #
