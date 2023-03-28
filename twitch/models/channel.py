class Channel():

    def __init__(self, data: dict) -> None:
        self.broadcaster_id: str = data.get("broadcaster_id", None)
        self.broadcaster_login: str = data.get("broadcaster_login", None)
        self.broadcaster_name: str = data.get("broadcaster_name", None)
        self.broadcaster_language: str = data.get("broadcaster_language", None)
        self.game_name: str = data.get("game_name", None)
        self.game_id: str = data.get("game_id", None)
        self.title: str = data.get("title", None)
        self.delay: int = data.get("delay", None)
        self.tags: list = data.get("tags", [])
