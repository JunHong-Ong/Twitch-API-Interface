from typing import Dict

class CheermoteTier():

    def __init__(self, data: Dict) -> None:
        self.min_bits: int = data.get("min_bits", None)
        self.id: str = data.get("id", None)
        self.color: str = data.get("color", None)
        self.images: dict = data.get("images", None)
        self.can_cheer: bool = data.get("can_cheer", None)
        self.show_in_bits_card: bool = data.get("show_in_bits_card", None)

class Cheermote():

    def __init__(self, data: Dict) -> None:
        self.prefix: str = data.get("prefix", None)
        self.tiers: list = [CheermoteTier(tier) for tier in data.get("tiers", [])]
        self.type: str = data.get("type", None)
        self.order: int = data.get("order", None)
        self.last_updated: str = data.get("last_updated", None)
        self.is_charitable: bool = data.get("is_charitable", None)
