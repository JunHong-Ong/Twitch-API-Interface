"""TODO: INSERT DOCSTRING"""

from typing import Union

class Video():

    def __init__(self, data: dict) -> None:
        self.id: str = data.get("id", None)
        self.stream_id: str = data.get("stream_id", None)
        self.user_id: str = data.get("user_id", None)
        self.user_login: str = data.get("user_login", None)
        self.user_name: str = data.get("user_name", None)
        self.title: str = data.get("title", None)
        self.description: str = data.get("description", None)
        self.created_at: str = data.get("created_at", None)
        self.published_at: str = data.get("published_at", None)
        self.url: str = data.get("url", None)
        self.thumbnail_url: str = data.get("thumbnail_url", None)
        self.viewable: str = data.get("viewable", None)
        self.view_count: int = data.get("view_count", None)
        self.language: str = data.get("language", None)
        self.type: str = data.get("type", None)
        self.duration: str = data.get("duration", None)
        self.muted_segments: list[dict[str, int]] = data.get("muted_segments", None)
