# sequence_processor.py
from abc import ABC, abstractmethod

class SequenceProcessorBase(ABC):
    @abstractmethod
    def process_sequence(self):
        # Abstract method to process a sequence of numbers
        pass

class SequenceConverter:
    def __init__(self, sequence):
        # Initialize with the input sequence and an empty list for numerical values
        self.sequence = sequence
        self.numerical_values = []

    def convert_to_numeric_list(self):
        # Convert the input sequence into a list of numerical values
        in_z_sequence = False
        z_accumulated_sum = 0

        for char in self.sequence:
            # Determine the offset value for ASCII mapping
            offset_val = 97 if char != "_" else 96
            # Convert character to numerical value based on ASCII and 'z' sequence logic
            char_value = ord(char) - offset_val + 1

            if char == "z":
                # Track if in 'z' sequence and accumulate sum
                in_z_sequence = True
                z_accumulated_sum += char_value
            else:
                in_z_sequence = False
                if not in_z_sequence:
                    if z_accumulated_sum > 0:
                        # Add accumulated sum and reset if not in 'z' sequence
                        z_accumulated_sum += char_value
                        self.numerical_values.append(z_accumulated_sum)
                        z_accumulated_sum = 0
                    else:
                        # Add character value if not in 'z' sequence
                        self.numerical_values.append(char_value)
                elif char == "_":
                    # Append accumulated sum if encounter '_' and reset
                    self.numerical_values.append(z_accumulated_sum)
                    z_accumulated_sum = 0
                    in_z_sequence = False

        return self.numerical_values

class CompressedSequenceProcessor(SequenceProcessorBase):
    def __init__(self, numerical_values):
        # Initialize with the numerical values
        self.numerical_values = numerical_values

    def process_sequence(self):
        # Process numerical values to generate compressed sequence
        compressed_values = []
        is_step = True
        step_remaining = 0
        current_sum = 0

        for num in self.numerical_values:
            if is_step:
                # Set current number as a step if True
                step_remaining = num
                is_step = False
            elif step_remaining > 0:
                # Accumulate numbers until step_remaining reaches 0
                current_sum += num
                step_remaining -= 1

                if step_remaining == 0:
                    # Append the result and reset cycle when step_remaining is 0
                    compressed_values.append(current_sum)
                    current_sum = 0
                    is_step = True

        return compressed_values

def sequence_compressor(sequence):
    # Main function to convert a sequence into compressed values
    converter = SequenceConverter(sequence)
    numerical_values = converter.convert_to_numeric_list()

    if not numerical_values:
        return ["Invalid Input"]
    print("Numerical Values:", numerical_values)
    processor = CompressedSequenceProcessor(numerical_values)
    print("Measured Inflows:")
    return processor.process_sequence()
