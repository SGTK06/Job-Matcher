"""
File to test the API call handle class
author: Sham Ganesh Thamarai Kannan
for: FIT2107 D2
"""
import unittest
from unittest import mock

import requests

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
1. Successful caller creation
2. Return empty dictionary on connection timeout
3. Return empty dictionary on facing network issues
4. Proxy creation as per proxy provider (webshare) format
"""

def simulate_await_timeout(url, headers=None, proxies=None, timeout=None):
    """since requests enforces timeout,
    after timeout time it will raise the
    error, due to mock, raise error here
    directly"""
    raise requests.exceptions.Timeout("Timeout Error")

def simulate_network_error(url, headers=None, proxies=None, timeout=None):
    """since requests checks for network,
    after connection failure it will raise the
    error, due to mock, raise error here
    directly"""
    raise requests.exceptions.ConnectionError("Network Connection Error")

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

    def test_caller_creation_wt1(self):
        """
        Test if the caller object is successfully.
        (testing __init__)
        """
        new_caller = ApiRequest()
        self.assertTrue(True)

    @mock.patch("requests.Session.get", side_effect=simulate_await_timeout)
    def test_simulate_connection_timeout_wt2(self, timeout):
        """
        use mocking to simulate connection timeout
        -> use requests exeption for timeout
        """
        resp = self.caller.get_request(REMOTIVE_API, 5)
        timeout_empty_return = {}
        self.assertEqual(resp, timeout_empty_return)

    @mock.patch("requests.Session.get", side_effect=simulate_network_error)
    def test_simulate_network_error_wt2(self, network):
        """
        use mocking to simulate connection timeout
        -> use requests exeption for timeout
        """
        resp = self.caller.get_request(REMOTIVE_API, 5)
        failed_connection_empty_return = {}
        self.assertEqual(resp, failed_connection_empty_return)

    def test_proxy_header(self):
        proxy_headers = self.caller.create_rotating_proxy(
            "proxyName",
            "proxyAuth"
        )
        expected_webshare_headers = {
            "http": f"http://proxyName:proxyAuth@p.webshare.io:80/",
            "https": f"http://proxyName:proxyAuth@p.webshare.io:80/"
        }
        self.assertEqual(proxy_headers, expected_webshare_headers)


