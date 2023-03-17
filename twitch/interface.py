"""TODO: INSERT MODULE DOCSTRING"""

from typing import Union, Any

import logging
import requests
import aiohttp
import time
import math


logger = logging.getLogger(__name__)

class Token():
    """TODO: INSERT CLASS DOCSTRING"""

    def __init__(self, data: dict[str, Union[str, int]]) -> None:
        self._data = data

    def __repr__(self) -> str:
        return f'Bearer {self._data.get("access_token")}'

    @property
    def id(self):
        """Returns the access token value"""
        return self._data.get("access_token")

class HelixInterface():

    _BASE_URL = "https://api.twitch.tv/helix"
    request_rate = 0.1

    def __init__(self, client_id, client_secret) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
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

    async def get_clip(self, session, clip_id):
        async with session.get("https://api.twitch.tv/helix/clips",
                               headers=self.headers,
                               params={"id":clip_id,"first":100}) as response:
            return response

    def _callback(self, task):
        headers, _ = task.result()
        remaining = int(headers.get("RateLimit-Remaining"))
        reset = int(headers.get("RateLimit-Reset"))
        time_to_reset = max(math.floor(reset - time.time()), 0)

        if remaining == 0:
            self.request_rate = time_to_reset
        else:
            self.request_rate = min(time_to_reset/remaining, 1)

    async def request(self, session: aiohttp.ClientSession, method, url, params=None, data=None, json=None):
        async with session.request(method,
                                   url,
                                   params=params,
                                   data=data,
                                   json=json,
                                   headers=self.headers) as response:
            
            if self._successful_response(response):
                return response.headers, await response.json()
            else:
                self._retry()

    async def get(self, session: aiohttp.ClientSession, endpoint: str, params=None, data=None, json=None):
        url = self._BASE_URL + "/" + endpoint
        return await self.request(session, "GET", url, params=params, data=data, json=json)

    async def post(self, session: aiohttp.ClientSession, endpoint: str, params=None, data=None, json=None):
        url = self._BASE_URL + "/" + endpoint
        return await self.request(session, "POST", url, params=params, data=data, json=json)

    def _successful_response(self, response):
        return response.status == 200
    
    def _retry(self):
        raise NotImplementedError
