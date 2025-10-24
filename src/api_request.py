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
        rotating_proxies = {
            "http": f"http://{proxy_name}:{proxy_auth}@p.webshare.io:80/",
            "https": f"http://{proxy_name}:{proxy_auth}@p.webshare.io:80/"
        }
        return rotating_proxies

    def get_request(self, url, query_limit):
        """
        function to query API url and return the response of API
        as a json object.
        inputs:
         - url : API url link
         - query_limit : limit on response of API
        returns:
         - response : in json format
         """
        if query_limit is not None:
            url = url + f"?limit={query_limit}"

        response = self.request_session.get(
            url,
            headers=self.access_headers,
            proxies=self.rotating_proxy
        )

        if response.status_code == 200:
            return response.json()
        else:
            # fallback to normal query
            response = self.request_session.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                print("ERROR FETCHING DATA USING API")
                return {}
