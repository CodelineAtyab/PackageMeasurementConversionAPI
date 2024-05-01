import unittest
import cherrypy
from main_app import SequenceConverterAPI

class TestMainApp(unittest.TestCase):
    def setUp(self):
        # Create an instance of the SequenceConverterAPI
        self.api = SequenceConverterAPI()
        # Mount the API to a test server
        self.server = cherrypy.tree.mount(self.api, '/')

    def test_convert_measurements(self):
        # Test cases for different inputs and their expected outputs
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
            ("zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_", [26])
        ]

        # Iterate through test cases and run sub-tests
        for input_str, expected_output in test_cases:
            # Mock the request with input parameters
            request = self.mock_request({'input': input_str})
            # Call the API endpoint with the mock request
            result = self.call_api_endpoint(request)
            # Assert the result matches the expected output
            self.assertEqual(result, expected_output)

    def mock_request(self, params):
        # Define a mock request class
        class MockRequest:
            pass
        # Create an instance of the mock request with parameters
        request = MockRequest()
        request.params = params
        return request

    def call_api_endpoint(self, request):
        # Call the API endpoint with the mock request and return the result
        return self.server.request_class.convert_measurements(self.api, **request.params)

if __name__ == '__main__':
    unittest.main()


