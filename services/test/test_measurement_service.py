import unittest
from services.measurement_service import convert_measurements

class TestConvertMeasurements(unittest.TestCase):
    """
    A group of unit tests for the 'convert_measurements' function.
    """

    def test_string_with_double_letters(self):
        # Directly use the function with the appropriate input.
        result = convert_measurements('aa')
        self.assertEqual(result, [1])  # Adjust expected result as necessary based on actual function logic.

    def test_string_multiple_letters(self):
        result = convert_measurements('abbcc')
        self.assertEqual(result, [2, 6])  # Assuming this is what convert_measurements should return.

    def test_string_with_underscore(self):
        result = convert_measurements('dz_a_aazzaaa')
        self.assertEqual(result, [28, 53, 1])  # Adjust based on actual logic.

    def test_string_with_one_letter_underscore(self):
        result = convert_measurements('a_')
        self.assertEqual(result, [0])

    def test_valid_string1(self):
        result = convert_measurements('abcdabcdab')
        self.assertEqual(result, [2, 7, 7])

    def test_string_ending_with_underscore(self):
        result = convert_measurements('abcdabcdab_')
        self.assertEqual(result, [2, 7, 7, 0])

    def test_string_starting_with_z(self):
        result = convert_measurements('zdaaaaaaaabaaaaaaaabaaaaaaaabbaa')
        self.assertEqual(result, [34])

if __name__ == "__main__":
    unittest.main(verbosity=2)
