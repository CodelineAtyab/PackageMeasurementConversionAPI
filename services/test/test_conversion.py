import unittest
from services.converter import PackageConverter


class TestPackageConverter(unittest.TestCase):
    def setUp(self):
        self.converter = PackageConverter()

    def test_single_characters(self):
        """Test conversion of single-character strings."""
        self.assertEqual(self.converter.convert_measurements("aa"), [1])
        self.assertEqual(self.converter.convert_measurements("__"), [0])
        self.assertEqual(self.converter.convert_measurements("a_"), [0])

    def test_multiple_characters(self):
        """Test conversion of strings with multiple characters."""
        self.assertEqual(self.converter.convert_measurements('abbcc'), [2, 6])
        self.assertEqual(self.converter.convert_measurements('abcdabcdab'), [2, 7, 7])
        self.assertEqual(self.converter.convert_measurements('abcdabcdab_'), [2, 7, 7, 0])

    def test_invalid_sequences(self):
        """Test conversion of strings that are expected to be invalid."""
        self.assertEqual(self.converter.convert_measurements("abz"), "Invalid")
        self.assertEqual(self.converter.convert_measurements("aaa"), "Invalid")
        self.assertEqual(self.converter.convert_measurements("abc"), "Invalid")

    def test_edge_cases(self):
        """Test conversion of strings with edge cases."""
        self.assertEqual(self.converter.convert_measurements('dz_a_aazzaaa'), [28, 53, 1])
        self.assertEqual(self.converter.convert_measurements('_zzzb'), [0])


if __name__ == '__main__':
    unittest.main()
