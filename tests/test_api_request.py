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
2. Return empty dictionary on connection timeout
3. Return empty dictionary on facing network issues
4. Return empty dictionary on requesting response from fake API/URL
"""
class TestApiRequest(unittest.TestCase):
    """
    class to test if the API caller works as expected
    """
    def test_response_format(self):
        """
        tests if the caller returns a dictionary (
        json format in python)
        """
        caller = ApiRequest()
        resp = caller.get_request(REMOTIVE_API, 5)
        self.assertEqual(type(resp), dict)