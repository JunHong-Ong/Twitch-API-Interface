class Game():

    def __init__(self, data: dict) -> None:
        self.id: str = data.get("id", None)
        self.name: str = data.get("name", None)
        self.box_art_url: str = data.get("box_art_url", None)
        self.igdb_id: str = data.get("igdb_id", None)
