class Measurements:
    def __init__(self):
        self.alpha_value = {chr(i): i - 96 for i in range(97, 123)}  # Dictionary to map 'a' to 'z' to 1-26

    def convert_character(self, char):
        """Convert a single alphabetic character to its numeric value or handle special characters."""
        if char == '_':
            return None  # None signifies a break or reset
        return self.alpha_value.get(char, 0)  # Returns 0 for non-alphabetic characters

    def convert_measurements(self, input_string):
        """Converts a string of characters into a list of numeric values, handling resets with '_'. """
        results = []
        current_sum = 0

        for char in input_string:
            value = self.convert_character(char)
            if value is None:  # Reset condition
                results.append(current_sum)
                current_sum = 0
            else:
                current_sum += value

        if current_sum > 0:  # Add any remaining sum to the results
            results.append(current_sum)

        return results

    def measurement_results(self, input_str):
        """Processes a list of numbers to handle measurement steps and aggregations."""
        numbers = self.convert_measurements(input_str)
        results = []
        step_count = 0
        current_sum = 0

        for num in numbers:
            if step_count == 0:  # We are expecting a new step count
                step_count = num
            else:
                current_sum += num
                step_count -= 1

                if step_count == 0:  # We have reached a complete set, reset and store the result
                    results.append(current_sum)
                    current_sum = 0

        return results
