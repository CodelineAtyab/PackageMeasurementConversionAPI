import unittest

from ..SequenceService import SequenceService


CURRENT_VS_EXPECTED_VALUE = (
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


class TestSequence(unittest.TestCase):

    def test_sequence(self):
        for test_string, expected in CURRENT_VS_EXPECTED_VALUE:
            sequence_service = SequenceService()
            sequence_service.get_sequence(test_string)
            result = sequence_service.process_sequence()
            print(f"result {result} expected {expected}")
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()