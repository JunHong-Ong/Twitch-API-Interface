"""This module allow users to send various HTTP requests to the Twitch Helix API.
It implements the HelixInterface and Token classes
"""

from typing import Union, Any

import logging
import requests
from requests import Response

logger = logging.getLogger(__name__)

class Token():
    """The Token class stores data received from the OAuth Client Credentials Flow"""

    def __init__(self, data: dict[str, Union[str, int]]) -> None:
        self._data = data

    def __repr__(self) -> str:
        return f'Bearer {self._data.get("access_token")}'

    @property
    def value(self):
        """Returns the access token value"""
        return self._data.get("access_token")

class HelixInterface():
    """ The HelixInterface class allow users to send and receive HTTP requests
        and responses from the Twitch Helix API. 
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.token = self._get_app_access_token(client_id, client_secret)
        self.headers = {"Authorization": str(self.token), "Client-Id": client_id}

    def _get_app_access_token(self, client_id: str, client_secret: str) -> Token:
        """ Requests an app access token from the oauth endpoint. """

        params = {
            "client_id":client_id,
            "client_secret":client_secret,
            "grant_type":"client_credentials"
        }

        response = requests.request("POST", "https://id.twitch.tv/oauth2/token", params=params,
                                        timeout=5)

        if response.status_code == 200:
            return Token(response.json())

        raise ValueError(response.json().get("message"))

    def send(self, method, url, headers=None, params=None, json=None) -> Response:
        return requests.request(method, url, headers=headers, params=params, json=json)