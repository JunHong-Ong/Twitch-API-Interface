"""TODO: INSERT MODULE DOCSTRING"""

from typing import Union, Generator

import asyncio
import aiohttp

from .interface import HelixInterface
from .helix_resources import Video, Channel, Clip



class Helix:
    def __init__(self, client_id, client_secret) -> None:
        self.interface = HelixInterface(client_id, client_secret)

    async def channels(self, *broadcaster_ids):
        ENDPOINT = "channels"

        tasks = set()
        group_size = 100

        async with aiohttp.ClientSession() as session:
            for index, group in enumerate(self._group(group_size, *broadcaster_ids)):
                task = asyncio.ensure_future(self.interface.get(session, ENDPOINT, params={"broadcaster_id":group,"first":100}))
                task.set_name(f"Group {index}: broadcaster IDs {(index-1)*group_size} - {min((index)*group_size, len(broadcaster_ids))}")
                task.add_done_callback(self.interface._callback)
                tasks.add(task)
                asyncio.gather(*tasks)

                await asyncio.sleep(self.interface.request_rate)

            responses = await asyncio.gather(*tasks)

        return responses

    async def clips(self, *clip_ids):
        ENDPOINT = "clips"

        tasks = set()
        group_size = 100

        async with aiohttp.ClientSession() as session:
            for index, group in enumerate(self._group(group_size, *clip_ids)):
                task = asyncio.ensure_future(self.interface.get(session, ENDPOINT, params={"id":group,"first":100}))
                task.set_name(f"Group {index}: Clip IDs {(index-1)*group_size} - {min((index)*group_size, len(clip_ids))}")
                task.add_done_callback(self.interface._callback)
                tasks.add(task)
                asyncio.gather(*tasks)

                await asyncio.sleep(self.interface.request_rate)

            responses = await asyncio.gather(*tasks)

        responses = [Clip(data) for response in responses for data in response[1]["data"]]

        for response in responses:
            yield response

    async def users(self, *user_ids):
        ENDPOINT = "users"

        tasks = set()
        group_size = 100

        async with aiohttp.ClientSession() as session:
            for index, group in enumerate(self._group(group_size, *user_ids)):
                task = asyncio.ensure_future(self.interface.get(session, ENDPOINT, params={"id":group,"first":100}))
                task.set_name(f"Group {index}: Clip IDs {(index-1)*group_size} - {min((index)*group_size, len(user_ids))}")
                task.add_done_callback(self.interface._callback)
                tasks.add(task)
                asyncio.gather(*tasks)

                await asyncio.sleep(self.interface.request_rate)

            responses = await asyncio.gather(*tasks)

        return responses

    async def videos(self, *video_ids):
        ENDPOINT = "videos"

        tasks = set()
        group_size = 100

        async with aiohttp.ClientSession() as session:
            for index, group in enumerate(self._group(group_size, *video_ids)):
                task = asyncio.ensure_future(self.interface.get(session, ENDPOINT, params={"id":group,"first":100}))
                task.set_name(f"Group {index}: Clip IDs {(index-1)*group_size} - {min((index)*group_size, len(video_ids))}")
                task.add_done_callback(self.interface._callback)
                tasks.add(task)
                asyncio.gather(*tasks)

                await asyncio.sleep(self.interface.request_rate)

            responses = await asyncio.gather(*tasks)

        return responses


    def _group(self, group_size, *inputs):
        num_inputs = len(inputs)
        groups = [
            inputs[i:i+group_size]
            for i in range(0, num_inputs, group_size)
        ]
        num_groups = len(groups)

        print(f"{num_inputs} inputs has been divided into {num_groups} groups of size {group_size}.")
        return groups
