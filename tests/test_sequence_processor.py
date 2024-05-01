import unittest
from Services.sequence_processor import sequence_compressor

class TestSequenceProcessor(unittest.TestCase):
    def test_sequence_compressor(self):
        # Define test cases with input sequences and expected outputs
        test_cases = [
            ("dz_a_aazzaaa", [28, 53, 1]),
            ("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa", [40, 1]),
            ("aa", [1]),
            ("abbcc", [2, 6]),
            ("a_", [0]),
            ("abcdabcdab", [2, 7, 7]),
            ("abcdabcdab_", [2, 7, 7, 0]),
            ("zdaaaaaaaabaaaaaaaabaaaaaaaabbaa", [34]),
            ("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa", [40, 1]),
            ("zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_", [26])
        ]

        # Iterate through test cases and run sub-tests
        for sequence, expected_output in test_cases:
            with self.subTest(sequence=sequence):
                # Call sequence_compressor function with each sequence
                result = sequence_compressor(sequence)
                # Assert the result matches the expected output
                self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
