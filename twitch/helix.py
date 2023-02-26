from typing import Union, Any

from .interface import HelixInterface

class Helix():

    def __init__(self, client_id, client_secret) -> None:
        self.interface = HelixInterface(client_id, client_secret)

    def get_videos(self, *video_ids: Union[str, int]) -> dict[str, Any]:

        endpoint = "videos"

        # Check data types of video_ids provided
        if len(video_ids) == 1:
            if type(video_ids[0]) not in [str, int]:
                raise TypeError("video_id must be of type str or int.")
            else:
                try:
                    int(video_ids[0])
                except:
                    raise ValueError("The video_id provided cannot be converted into an integer.")
        else:
            if not all([type(video_id) in [str, int] for video_id in video_ids]):
                raise TypeError("video_ids must be of type str or int.")
            else:
                try:
                    [int(video_id) for video_id in video_ids]
                except:
                    raise ValueError("One or more video_ids provided cannot be converted into an integer.")
        
        # Chunks video_ids into batches of max 100
        if len(video_ids) <= 100:
            params = {"id": video_ids}
        else:
            params = {"id": video_ids[:100]}
            self.get_videos(*video_ids[100:])

        response = self.interface.get(endpoint, headers=self.interface.headers, params=params)

        return response.json()["data"]
