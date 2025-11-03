"""
File with API call handle class
author: Sham Ganesh Thamarai Kannan
for: FIR2107 D2
"""
import requests
from fake_useragent import UserAgent
from src.config import PROXY_NAME, PROXY_AUTH


class ApiRequest:
    """
    class to handle the API call requests made by
    Job Matcher
    """
    def __init__(self):
        """class to construct call handler"""
        self.access_headers = {
            "User-Agent": UserAgent().random,
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Referer": "https://www.google.com"
        }
        self.rotating_proxy = self.create_rotating_proxy(PROXY_NAME, PROXY_AUTH)
        self.request_session = requests.Session()

    def create_rotating_proxy(self, proxy_name, proxy_auth):
        """
        creates rotating proxies to avoid rate limit or same ip
        problems for more reliable api querying
        """
        rotating_proxies = {
            "http": f"http://{proxy_name}:{proxy_auth}@p.webshare.io:80/",
            "https": f"http://{proxy_name}:{proxy_auth}@p.webshare.io:80/"
        }
        return rotating_proxies

    def get_request(self, url, query_limit=None):
        """
        function to query API url and return the response of API
        as a json object.
        inputs:
         - url : API url link
         - query_limit : limit on response of API
        returns:
         - response : in json format
         """
        try:
            if query_limit is not None:
                url = url + f"?limit={query_limit}"

            response = self.request_session.get(
                url,
                headers=self.access_headers,
                proxies=self.rotating_proxy,
                timeout=15
            )

            if response.status_code == 200:
                return response.json()

            # fallback to normal query
            response = self.request_session.get(
                url,
                timeout=5
            )

            if response.status_code == 200:
                return response.json()

            print("ERROR FETCHING DATA USING API")
            return {}

        except requests.exceptions.RequestException as req_except:
            """
            source: https://www.geeksforgeeks.org/python/exception-handling-of-python-requests-module/
            exception handler for all the request exception
             - invalid URL
             - invalid format
             - connection timeout
             - network error
             etc.
            """
            print(req_except)
            return {}

