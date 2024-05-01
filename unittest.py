import unittest
from main_app import MeasurementService

class TestMeasurementService(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test method."""
        self.service = MeasurementService()

    def tearDown(self):
        """Clean up test environment after each test method."""
        pass

    def test_conversion(self):
        """Test conversion functionality."""
        test_cases = [
            ("aa", [1]),
            ("abbcc", [2, 6]),
            ("a_", [0]),
            ("abcdabcdab", [2, 7, 7]),
            ("abcdabcdab_", [2, 7, 7, 0]),
            ("zdaaaaaaaabaaaaaaaabaaaaaaaabbaa", [34]),
            ("zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_", [26]),
            ("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa", [40, 1]),
            ("_", [0]),
            ("_ad", [0]),
            ("a_", [0]),
            ("_zzzb", [0]),
            ("__", [0])
        ]
        for input_str, expected_output in test_cases:
            with self.subTest(input_str=input_str):
                output = self.service.convert_measurements(input_str)
                self.assertEqual(output, expected_output, f"Conversion incorrect for input '{input_str}'")

    def test_conversion_results(self):
        """Test conversion results functionality."""
        test_cases = [
            ("aa", [1]),
            ("abbcc", [2, 6]),
            ("a_", [0]),
            ("abcdabcdab", [2, 7, 7]),
            ("abcdabcdab_", [2, 7, 7, 0]),
            ("zdaaaaaaaabaaaaaaaabaaaaaaaabbaa", [34]),
            ("zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_", [26]),
            ("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa", [40, 1]),
            ("_", [0]),
            ("_ad", [0]),
            ("a_", [0]),
            ("_zzzb", [0]),
            ("__", [0])
        ]
        for input_str, expected_results in test_cases:
            with self.subTest(input_str=input_str):
                results = self.service.measurement_results(input_str)
                self.assertEqual(results, expected_results, f"Conversion results incorrect for input '{input_str}'")

if __name__ == "__main__":
    unittest.main()
