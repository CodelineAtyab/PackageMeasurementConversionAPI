class Measurements(object):
    def __init__(self):
        pass

    def convert_measurements(self, input_string):
        # Initialize the results list and the current sum.
        results = []
        current_sum = 0

        # Keep track of the count for each input
        input_count = 0

        # Loop through each character in the input string.
        for char in input_string:
            if char == '_':
                # When facing an underscore, append the current sum to results then reset it to 0.
                results.append(current_sum)
                current_sum = 0
                input_count = 0
            elif 'a' <= char <= 'z':
                # Convert the alphabet to their number value (a=1, b=2, etc..).
                input_count += 1
                current_sum += ord(char) - ord('a') + 1

            if input_count > 0 and current_sum > 0:
                # append the sum to the result list if input_count and current sum have a value
                results.append(current_sum)
                current_sum = 0
                input_count = 0

        return results

    def measurement_results(self, input_str):
        # Convert the input str from the url into a list of numbers then start the count

        list_of_num = self.convert_measurements(input_str)
        result_input_list = []
        is_a_step = True  # First character/number = step one.
        step_count_remaining = 0  # Set the count as soon as the number is encountered.
        curr_input_sum = 0  # continue adding the values until remaining step count != 0
        i = 0
        for curr_num in list_of_num:
            i += 1
            if is_a_step:
                if curr_num == 26:  # Check if current character is Z count
                    step_count_remaining += curr_num
                elif curr_num == 0:  # Check if current Character is underscore
                    result_input_list.append(0)
                    break
                else:
                    step_count_remaining += curr_num
                    is_a_step = False
            elif step_count_remaining > 0:
                if curr_num == 26:
                    curr_input_sum += curr_num
                else:
                    curr_input_sum += curr_num
                    step_count_remaining -= 1

            if step_count_remaining == 0:  # append the measurement result then reset the count before exiting
                result_input_list.append(curr_input_sum)
                curr_input_sum = 0
                step_count_remaining = 0
                is_a_step = True
            elif step_count_remaining > (len(list_of_num) - 1) - i:
                result_input_list = []

        return result_input_list
