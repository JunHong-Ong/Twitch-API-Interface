from typing import Union, Any

from .interface import HelixInterface

class Helix():

    BASE_URL = "https://api.twitch.tv/helix/"

    def __init__(self, client_id, client_secret) -> None:
        self.interface = HelixInterface(client_id, client_secret)

    def get_videos(self, *video_ids: Union[str, int]) -> dict[str, Any]:
        
        endpoint = "videos"
        print(video_ids)

        # Check data types of video_ids provided
        if len(video_ids) == 1:
            if type(video_ids[0]) not in [str, int]:
                raise TypeError("video_id must be of type str or int.")
            else:
                try:
                    int(video_ids[0])
                except:
                    raise ValueError("The video_id provided cannot be converted into an integer.")
        elif len(video_ids) > 1 and len(video_ids) <= 100:
            if not all([type(video_id) in [str, int] for video_id in video_ids]):
                raise TypeError("video_ids must be of type str or int.")
            else:
                try:
                    [int(video_id) for video_id in video_ids]
                except:
                    raise ValueError("One or more video_ids provided cannot be converted into an integer.")
        
        params = {"id": video_ids}

        response = self.get(endpoint, headers=self.interface.headers, params=params)

        return response.json()["data"]
            
    
    def get(self, endpoint, headers=None, params=None, json=None):
        url = self.BASE_URL + endpoint

        return self.interface.send("GET", url, headers, params, json)

    def post(self, endpoint, headers=None, params=None, json=None):
        url = self.BASE_URL + endpoint

        return self.interface.send("POST", url, headers, params, json)