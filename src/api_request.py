import requests

class ApiRequest:
    """
    class to handle the API call requests made by
    Job Matcher
    """
    def __init__(self):
        """class to construct call handler"""

    def get_request(self ,url, query_limit):
        """
        function to query API url and return the response of API
        as a json object.
        inputs:
         - url : API url link
         - query_limit : limit on response of API
        returns:
         - response : in json format
         """