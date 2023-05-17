from dataclasses import dataclass
import requests


@dataclass
class Response:
    """Response formatting as dict"""
    status_code: int
    text: str
    as_dict: object
    headers: dict


class APIRequest:
    """API Requests"""

    def get(self, url):
        "API Get Request"
        response = requests.get(url)
        return APIRequest.__get_response(response)

    def post(self, url, payload, headers):
        "API Post Request"
        response = requests.post(url, data=payload, headers=headers)
        return APIRequest.__get_response(response)

    @staticmethod
    def __get_response(response):
        "For formatting the response"
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception as er_msg:
            as_dict = {}
            print("Exception %s", er_msg)

        headers = response.headers

        return Response(status_code, text, as_dict, headers)
