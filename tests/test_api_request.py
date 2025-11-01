"""
File to test the API call handle class
author: Sham Ganesh Thamarai Kannan
for: FIT2107 D2
"""
import unittest

from src.api_request import ApiRequest
from src.config import REMOTIVE_API

"""
Tests that check whether the API response has expected format
and API caller functions as expected.

Blackbox Tests:
Expected:
1. Returns a response in JSON format (python dictionary): https://github.com/remotive-com/remote-jobs-api
2. Return empty dictionary on requesting response from fake API/URL

Whitebox Tests:
Expected:
1. Return empty dictionary on connection timeout
2. Return empty dictionary on facing network issues
"""
class TestApiRequest(unittest.TestCase):
    """
    class to test if the API caller works as expected
    code: btX -> bt - black box test, X-test number
          wtX -> bt - white box test, X-test number
    """
    def setUp(self):
        """create the caller object"""
        self.caller = ApiRequest()

    def test_response_format_bt1(self):
        """
        tests if the caller returns a dictionary (
        json format in python)
        """
        resp = self.caller.get_request(REMOTIVE_API, 5)
        self.assertEqual(type(resp), dict)

    def test_invalid_api_call_bt2(self):
        """
        tests if the caller returns an empty
        dictionary if a response is requested from
        invalid API
        """
        resp = self.caller.get_request("httpx://invalid-api.moc")
        empty_response = {}
        self.assertEqual(resp, empty_response)