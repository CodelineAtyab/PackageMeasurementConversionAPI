import unittest
from models.package_converter import PackageConverter


class TestPackageConverter(unittest.TestCase):
    """
    Two functions containing multiple test cases for valid and invalid user inputs
    """

    def setUp(self):
        self.converter = PackageConverter()

    def test_aa_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion("aa"), [1])

    def test_double_underscore_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion("__"), [0])

    def test_single_underscore_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion("a_"), [0])

    def test_abbcc_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion('abbcc'), [2, 6])

    def test_abcdabcdab_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion('abcdabcdab'), [2, 7, 7])

    def test_abcdabcdab_with_underscore_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion('abcdabcdab_'), [2, 7, 7, 0])

    def test_dz_a_aazzaaa_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion('dz_a_aazzaaa'), [28, 53, 1])

    def test_zdaaaaaaaabaaaaaaaabaaaaaaaabbaa_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion('zdaaaaaaaabaaaaaaaabaaaaaaaabbaa'), [34])

    def test_za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion('za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa'), [40, 1])

    def test_zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_underscore_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion('zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_'), [26])

    def test_single_underscore_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion("_"), [0])

    def test_underscore_ad_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion("_ad"), [0])

    def test_a_underscore_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion("a_"), [0])

    def test_underscore_zzzb_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion("_zzzb"), [0])

    def test_abz_invalid_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion("abz"), "Invalid")

    def test_aaa_invalid_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion("aaa"), "Invalid")

    def test_abc_invalid_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion("abc"), "Invalid")

    def test_baaca_invalid_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion("baaca"), "Invalid")

    def test_ccc_invalid_conversion(self):
        self.assertEqual(self.converter.package_measurement_conversion("ccc"), "Invalid")

if __name__ == '__main__':
    unittest.main()
