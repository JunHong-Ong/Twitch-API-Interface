"""TODO: INSERT MODULE DOCSTRING"""

from typing import Union, Generator

import asyncio
import aiohttp
import time
from warnings import warn

from .interface import HelixInterface
from .models import Video, Channel, Clip


class Helix:

    def __init__(self, client_id, client_secret) -> None:
        self.interface = HelixInterface(client_id, client_secret)

    async def videos(self, *video_ids):
        ENDPOINT = "videos"

        print(video_ids)
        # Check that only str and int are provided
        wrong_types = [ str(video_id) for video_id in video_ids
                        if type(video_id) not in [str, int] ]
        if len(wrong_types) != 0:
            raise TypeError(f"Video IDs: {', '.join(wrong_types)} are not of type str or int.")

        # Check that all strings are numeric
        non_numeric = [ str(video_id) for video_id in video_ids
                        if isinstance(video_id, str) and not video_id.isnumeric() ]
        if len(non_numeric) != 0:
            raise ValueError(f"Video IDs: {', '.join(non_numeric)} are non-numeric.")

        tasks = set()
        loop = asyncio.get_event_loop()

        for video_id in video_ids:
            params = {"id": video_id}
            task = loop.create_task(self.interface.get(
                "https://api.twitch.tv/helix/videos", self.interface.headers, params
            ))

            tasks.add(task)
            asyncio.gather(*tasks)
            await asyncio.sleep(self.interface._INITIAL_REQUEST_RATE)

        responses = await asyncio.gather(*tasks)

        return responses


    async def users(self, *user_ids_or_logins):
        ENDPOINT = "users"

        tasks = set()
        loop = asyncio.get_event_loop()

        user_ids_or_logins = [str(i) for i in user_ids_or_logins]
        for value in user_ids_or_logins:
            user_ids = [i for i in user_ids_or_logins if i.isdigit()]
            user_logins = [i for i in user_ids_or_logins if not i.isdigit()]
            
            params = {"id": user_ids, "login":user_logins}
            task = loop.create_task(self.interface.get(
                "https://api.twitch.tv/helix/users", self.interface.headers, params
            ))
            tasks.add(task)
            asyncio.gather(*tasks)
            await asyncio.sleep(self.interface._INITIAL_REQUEST_RATE)

        responses = await asyncio.gather(*tasks)

        return responses

    async def clips(self, *clip_ids):
        ENDPOINT = "clips"

        tasks = set()
        loop = asyncio.get_event_loop()

        for clip_id in clip_ids:
            params = {"id": clip_id}
            task = loop.create_task(self.interface.get(
                "https://api.twitch.tv/helix/clips", self.interface.headers, params
            ))

            tasks.add(task)
            asyncio.gather(*tasks)
            await asyncio.sleep(self.interface._INITIAL_REQUEST_RATE)

        responses = await asyncio.gather(*tasks)

        return responses
