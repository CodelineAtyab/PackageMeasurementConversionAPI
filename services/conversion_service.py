
class Conversion:

    def letter_value(self, letter: str):
        """
        A function to return the value associated with each letter
        :param letter: A single letter
        :return: An integer value of the inputted letter
        """
        value = ord(letter) - ord('a') + 1
        # print(f"The letter '{letter}' value is: {value}") # log statement to show the state of program
        return value

    def char_value(self, input_list):
        """
        A function that receives a list of letters/underscores and returns the integer values associated
        :param input_list: A list of alphabetic characters and/or underscores
        :return: A single integer value of each character
        """
        for char in input_list:
            if char == '_':
                # print(f"The _ value is: 0") # log statement to show the state of program
                return 0
            else:
                return self.letter_value(char)

    def get_merged_list(self, input_string):
        """
        A function to merge the value of z (26) with the next values
        :param input_string: A string given by the user
        :return: A merged list containing numeric values
        """
        merged_list = []
        merged_value = 0
        if len(input_string) > 0 and input_string[len(input_string)-1] == 26 :
            return "Invalid"
        else:
            for digit in input_string:
                if digit == 26:
                    merged_value += 26
                else:
                    merged_list.append(digit + merged_value)
                    merged_value = 0
        # print(f"The merged list is: {merged_list}")  # log statement to show the state of program
            return merged_list

    def converted_string(self, input_string):
        """
        A function which converts the input string to a list of the total values
        :param input_string: A sequence of characters
        :return: A result list containing the converted values
        """
        input_string = input_string.strip()
        allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_ ")
        for char in input_string:
            if char not in allowed_characters:
                return []
        char_list = [self.char_value(input_string[i]) for i in range(len(input_string))]
        result_list = []
        merged_list = self.get_merged_list(char_list)
        if merged_list == 'Invalid':
            return []
        else:
            while merged_list:
                counter = merged_list[0]
                if counter == 0:
                    result_list.append(0)
                    merged_list = []
                elif counter >= len(merged_list) or len(merged_list) < 1:
                    return []
                else:
                    merged_list.pop(0)
                    result_list.append(sum(merged_list[0:counter]))
                    merged_list = merged_list[counter:]

        if result_list and len(merged_list) == 0:
            return result_list
        else:
            return []

# # Check that the conversion is correct
# user_string = Conversion()
# print(user_string.converted_string("    "))


