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
5. If response code is wrong in attempt 1, use fallback logic
6. Check max 2 attempts
7. Return empty dictionary after 2 attempts
8. Test call count 1 in case of error

Mock Usage Documentation:

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


class RequestCountTracker:
    req_count = 0
    @classmethod
    def tracked_request(cls, url, headers=None, proxies=None, timeout=None):
        cls.req_count += 1
        return MockResp("invalid", 404)

    @classmethod
    def tracked_request_raises_exception(cls, url, headers=None, proxies=None, timeout=None):
        cls.req_count += 1
        raise requests.exceptions.RequestException

    @classmethod
    def reset_count(cls):
        cls.req_count = 0


class MockResp():
    def __init__(self, response, status_code):
        self.response = response
        self.status_code = status_code

    def json(self):
        return self.response


class TestApiRequest(unittest.TestCase):
    """
    class to test if the API caller works as expected
    code: btX -> bt - black box test, X-test number
          wtX -> bt - white box test, X-test number
    """
    def setUp(self):
        """create the caller object"""
        self.caller = ApiRequest()

    def tearDown(self):
        """reset count to prep for other test"""
        RequestCountTracker.reset_count()

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
    def test_simulate_network_error_wt3(self, network):
        """
        use mocking to simulate connection timeout
        -> use requests exeption for timeout
        """
        resp = self.caller.get_request(REMOTIVE_API, 5)
        failed_connection_empty_return = {}
        self.assertEqual(resp, failed_connection_empty_return)

    def test_proxy_header_creation_wt4(self):
        """
        test if webshare proxy headers are of the
        expected format
        """
        proxy_headers = self.caller.create_rotating_proxy(
            "proxyName",
            "proxyAuth"
        )
        expected_webshare_headers = {
            "http": f"http://proxyName:proxyAuth@p.webshare.io:80/",
            "https": f"http://proxyName:proxyAuth@p.webshare.io:80/"
        }
        self.assertEqual(proxy_headers, expected_webshare_headers)

    @mock.patch("requests.Session.get")
    def test_api_call_fallback_logic_wt5(self, mockRequest):
        """
        test if caller uses fallback method if first
        call returns invalid response status code
        """
        mockRequest.side_effect = [
            MockResp("invalid", 404),
            MockResp({"repsonse":"valid"}, 200)
        ]
        resp = self.caller.get_request(REMOTIVE_API, 5)
        second_call_response = {"repsonse":"valid"}
        self.assertEqual(resp, second_call_response)

    @mock.patch("requests.Session.get")
    def test_api_request_count_limit_wt6(self, mockRequest):
        """
        test to check of the maximum times the caller
        can query the api is 2.
        """
        mockRequest.side_effect = RequestCountTracker.tracked_request
        self.caller.get_request(REMOTIVE_API, 5)
        max_requests_allowed = 2
        self.assertTrue(RequestCountTracker.req_count <= max_requests_allowed)

    @mock.patch("requests.Session.get")
    def test_request_limit_exceeded_response_wt7(self, mockRequest):
        """
        test to check if the caller returns empty
        dictionary if call fails, no error raised.
        """
        mockRequest.side_effect = RequestCountTracker.tracked_request
        resp = self.caller.get_request(REMOTIVE_API, 5)
        count_exceeded_resp = {}
        self.assertEqual(resp, count_exceeded_resp)

    @mock.patch("requests.Session.get")
    def test_request_count_error_wt8(self, mockRequest):
        """
        test to check if the caller requests api
        repsone only once in case of error
        """
        mockRequest.side_effect = RequestCountTracker.tracked_request_raises_exception
        self.caller.get_request(REMOTIVE_API, 5)
        self.assertEqual(RequestCountTracker.req_count, 1)


