"""TODO: INSERT DOCSTRING"""

class Clip():
    """TODO: INSERT DOCSTRING"""

    def __init__(self, data: dict) -> None:
        self.id: str = data.get("id", None)
        self.url: str = data.get("url", None)
        self.embed_url: str = data.get("embed_url", None)
        self.broadcaster_id: str = data.get("broadcaster_id", None)
        self.broadcaster_name: str = data.get("broadcaster_name", None)
        self.creator_id: str = data.get("creator_id", None)
        self.creator_name: str = data.get("creator_name", None)
        self.video_id: str = data.get("video_id", None)
        self.game_id: str = data.get("game_id", None)
        self.language: str = data.get("language", None)
        self.title: str = data.get("title", None)
        self.view_count: int = data.get("view_count", None)
        self.created_at: str = data.get("created_at", None)
        self.thumbnail_url: str = data.get("thumbnail_url", None)
        self.duration: float = data.get("duration", None)
        self.vod_offset: str = data.get("vod_offset", None)
