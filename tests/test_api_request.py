import unittest

from src.api_request import ApiRequest
from src.config import REMOTIVE_API

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