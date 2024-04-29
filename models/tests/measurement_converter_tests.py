import unittest
from models.measurement_converter import MeasurementConverter


class TestMeasurementConverter(unittest.TestCase):

    def test_non_z_strings(self):
        """
        Test valid non z strings.
        """
        non_z_inputs = ["aa", "abbcc", "abcdabcdab", "a_" ]
        non_z_outputs = [[1], [2, 6], [2, 7, 7], [0]]

        for i in range(len(non_z_inputs)):
            self.assertEqual(MeasurementConverter().pmc(non_z_inputs[i]), non_z_outputs[i])
        
        
    def test_z_strings(self):
        """
        Test valid z strings.
        """
        z_inputs = ["dz_a_aazzaaa", "za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa", "zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_", "_zzzb", "_"]
        z_outputs = [[28, 53, 1], [40, 1], [26], [0], [0]]

        for i in range(len(z_inputs)):
            self.assertEqual(MeasurementConverter().pmc(z_inputs[i]), z_outputs[i])

    def test_invalid_strings(self):
        """
        Test invalid strings.
        """
        invalid_inputs = ["abc", "aaa", "z", "123", "+!@#"]

        for i in range(len(invalid_inputs)):
            self.assertEqual(MeasurementConverter().pmc(invalid_inputs[i]), "Invalid string input")


if __name__ == '__main__':
    unittest.main(verbosity=2)