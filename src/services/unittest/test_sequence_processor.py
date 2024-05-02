import unittest

from src.models.sequence import Sequence
from src.services.sequence_processor import SequenceProcessor

# tests to run
CURRENT_VS_EXPECTED_VALUE_MAPPING = (
    ("aa", [1]),
    ("abbcc", [2, 6]),
    ("dz_a_aazzaaa", [28, 53, 1]),
    ("a_", [0]),
    ("abcdabcdab", [2, 7, 7]),
    ("abcdabcdab_", [2, 7, 7, 0]),
    ("zdaaaaaaaabaaaaaaaabaaaaaaaabbaa", [34]),
    ("zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_", [26]),
    ("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa", [40, 1]),
    ("_", [0]),
    ("_ad", [0]),
    ("a_", [0]),
    ("_zzzb", [0]),
    ("__", [0])
)


class TestSequenceProcessor(unittest.TestCase):

    def test_sequence_processing(self):
        """
        Tests the logic of the Sequence processor and checks whether the result is as expected
        :return: Test OK
        """
        for test_string, expected in CURRENT_VS_EXPECTED_VALUE_MAPPING:
            sequence_instance = Sequence(test_string)
            processor = SequenceProcessor(sequence_instance)
            result = processor.create_result()
            print(f"result {result} expected {expected}")
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
