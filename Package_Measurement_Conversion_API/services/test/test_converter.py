import unittest
from Package_Measurement_Conversion_API.services.converter import Measurements


class TestPackageConverter(unittest.TestCase):
    # Testing both Valid and Invalid inputs

    def setUp(self):
        self.converter = Measurements()

    def test_conversion(self):
        self.assertEqual(self.converter.measurement_results("aa"), [1])
        self.assertEqual(self.converter.measurement_results("__"), [0])
        self.assertEqual(self.converter.measurement_results("a_"), [0])
        self.assertEqual(self.converter.measurement_results('abbcc'), [2, 6])
        self.assertEqual(self.converter.measurement_results('abcdabcdab'), [2, 7, 7])
        self.assertEqual(self.converter.measurement_results('abcdabcdab_'), [2, 7, 7, 0])
        self.assertEqual(self.converter.measurement_results('dz_a_aazzaaa'), [28, 53, 1])
        self.assertEqual(self.converter.measurement_results('zdaaaaaaaabaaaaaaaabaaaaaaaabbaa'), [34])
        self.assertEqual(self.converter.measurement_results('za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa'), [40, 1])
        self.assertEqual(self.converter.measurement_results('zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_'), [26])


if __name__ == '__main__':
    unittest.main()
