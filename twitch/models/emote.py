class Emote():

    def __init__(self, data: dict) -> None:
        self.id: str = data.get("id", None)
        self.name: str = data.get("name", None)
        self.images: dict = data.get("images", {})
        self.format: list = data.get("format", None)
        self.scale: list = data.get("scale", None)
        self.theme_mode: list = data.get("theme_mode", None)


class ChannelEmote(Emote):
        
    def __init__(self, data: dict) -> None:
        super().__init__(data)
        self.tier: str = data.get("tier", None)
        self.emote_type: str = data.get("emote_type", None)
        self.emote_set_id: str = data.get("emote_set_id", None)
        self.owner_id: str = data.get("owner_id", None)


class EmoteSet():

    def __init__(self, data: list) -> None:
        self.emotes = [ChannelEmote(emote) for emote in data]