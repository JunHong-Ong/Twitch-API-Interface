"""TODO: INSERT MODULE DOCSTRING"""

from typing import Union, Generator

from warnings import warn
from .interface import HelixInterface

from .helix_resources import Video

class Helix():
    """TODO: INSERT CLASS DOCSTRING"""

    def __init__(self, client_id, client_secret) -> None:
        self.interface = HelixInterface(client_id, client_secret)

    def get_videos(self, *video_ids: Union[str, int]) -> Generator[Video, None, None]:
        """Retrieves information of one or more videos.
        
        Videos are retrieved using their video ids.

        Parameters
        ----------
        *video_ids : str or int
            ID of videos to be retrieved.

        Yields
        ------
        Video
            A Video object representing information of one video.
        
        Examples
        --------
        >>> helix.get_videos(123456)

        >>> helix.get_videos("123456")

        Retrieving multiple videos.
         (IDs can be a combination of strings and integers).

        >>> helix.get_videos(123456, "234567", ... , 567890)
        """

        endpoint = "videos"
        print(video_ids)

        # Check that only str and int are provided
        wrong_types = [ str(video_id) for video_id in video_ids
                       if type(video_id) not in [str, int] ]
        if len(wrong_types) != 0:
            raise TypeError(f"Video IDs: {', '.join(wrong_types)} are not of type str or int.")

        # Check that all strings are numeric
        non_numeric = [ str(video_id) for video_id in video_ids
                       if isinstance(video_id, str) and not video_id.isnumeric() ]
        print(non_numeric)
        if len(non_numeric) != 0:
            raise ValueError(f"Video IDs: {', '.join(non_numeric)} are non-numeric.")

        # Chunks video_ids into batches of max 100
        if len(video_ids) <= 100:
            params = {"id": video_ids}
        else:
            params = {"id": video_ids[:100]}
            yield from self.get_videos(*video_ids[100:])

        response = self.interface.get(endpoint, headers=self.interface.headers, params=params)

        # Inform users of IDs which were not found
        ids_found = { str(data["id"]) for data in response.json()["data"] }
        ids_not_found = { str(video_id) for video_id in video_ids } - ids_found
        if len(ids_not_found) != 0:
            warn(f"Video IDs: {', '.join(ids_not_found)} could not be found.")

        for video_data in response.json()["data"]:
            yield Video(video_data)

    def get_channels(self):
        """TODO: INSERT DOCSTRING, Implement"""
        raise NotImplementedError
