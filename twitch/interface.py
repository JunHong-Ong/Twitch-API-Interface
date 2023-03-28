"""TODO: INSERT MODULE DOCSTRING"""

from typing import Optional

import logging
import requests
import aiohttp
import asyncio
import time
import math


logger = logging.getLogger(__name__)

class Token():

    def __init__(self, data: dict) -> None:
        self.access_token: str = data.get("access_token", None)
        self.expires_in: int = data.get("expires_in", None)
        self.token_type: str = data.get("token_type", None)


class HelixInterface():

    _BASE_URL = "https://api.twitch.tv/helix"
    _INITIAL_REQUEST_RATE = 60/800


    def __init__(self, client_id, client_secret) -> None:
        self.session: Optional[aiohttp.ClientSession] = None
        self.client_id = client_id
        self.token = self._get_token(client_id, client_secret)

    def _get_token(self, client_id: str, client_secret: str) -> Token:
        """Requests an app access token from the oauth endpoint."""

        params = {"client_id":client_id, "client_secret":client_secret,
            "grant_type":"client_credentials"}
        response = requests.request("POST", "https://id.twitch.tv/oauth2/token", params=params,
                                    timeout=5)

        if response.status_code == 200:
            return Token(response.json())
        
        raise ValueError(response.json().get("message"))

    @property
    def headers(self):
        return {"Authorization": f"Bearer {self.token.access_token}", "Client-Id": self.client_id}

    def _init_session(self):
        self.session = aiohttp.ClientSession()

    async def _close_session(self):
        if self.session is not None:
            await self.session.close()
            self.session = None

    async def get(self, url, headers, params):
        if self.session is None:
            self._init_session()

        if self.session is not None:
            async with self.session.get(url, headers=headers, params=params) as response:
                if response.status == 200:
                    rate_limit_remain = int(response.headers.get("RateLimit-Remaining", 0))
                    rate_limit_reset = int(response.headers.get("RateLimit-Reset", time.time()))
                    time_to_reset = max(math.floor(rate_limit_reset - time.time()), 0)

                    if rate_limit_remain == 0:
                        self._INITIAL_REQUEST_RATE = time_to_reset
                    else:
                        self._INITIAL_REQUEST_RATE = min(time_to_reset/rate_limit_remain, 1)

                    return (await response.json())