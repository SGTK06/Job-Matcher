import unittest

from src.api_request import ApiRequest
from src.config import REMOTIVE_API

class TestRemotiveApiResp(unittest.TestCase):
    """
    class to test if the API response is of expected format
    """
    def test_response_limit(self):
        """
        tests if the response has number of items
        enforced by query limit
        """
        caller = ApiRequest()
        resp = caller.get_request(REMOTIVE_API, 5)
        self.assertTrue(len(resp["jobs"]) <= 5)