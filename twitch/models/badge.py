class Badge():

    def __init__(self, data: dict) -> None:
        self.set_id: str = data.get("set_id", None)
        self.versions: list = data.get("versions", [])


class ChannelBadge(Badge):

    def __init__(self, data: dict) -> None:
        super().__init__(data)
        