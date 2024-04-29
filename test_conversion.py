import unittest

from models.conversion import Conversion


class TestConversion(unittest.TestCase):
    """
    A group of unit tests for the 'converted_string' function from the Conversion class
    """

    def test_string_with_double_letters(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('aa'), [1])

    def test_string_multiple_letters(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('abbcc'), [2, 6])

    def test_string_with_underscore(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('dz_a_aazzaaa'), [28, 53, 1])

    def test_string_with_one_letter_underscore(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('a_'), [0])

    def test_valid_string1(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('abcdabcdab'), [2, 7, 7])

    def test_string_ending_with_underscore(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('abcdabcdab_'), [2, 7, 7, 0])

    def test_string_starting_with_z(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('zdaaaaaaaabaaaaaaaabaaaaaaaabbaa'), [34])

    def test_string_starting_with_double_z(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_'), [26])

    def test_string_starting_with_z_a(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa'), [40, 1])

    def test_string_only_underscore(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('_'), [0])

    def test_string_starting_with_underscore(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('_ad'), [0])

    def test_string_starting_all_underscore(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('____'), [0])

    def test_invalid_string(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('aaa'), "Invalid input")

    def test_empty_string(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string(''), "Invalid input")

    def test_single_letter_string(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('a'), "Invalid input")

    def test_invalid_length_string(self):
        user_string = Conversion()
        self.assertEqual(user_string.converted_string('abccc'), "Invalid input")


if __name__ == "__main__":
    unittest.main(verbosity=2)
