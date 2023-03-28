from typing import Dict

class User():
    
    def __init__(self, data: dict) -> None:
        self.id: str = data.get("id", None)
        self.login: str = data.get("login", None)
        self.display_name: str = data.get("display_name", None)
        self.type: str = data.get("type", None)
        self.broadcaster_type: str = data.get("broadcaster_type", None)
        self.description: str = data.get("description", None)
        self.profile_image_url: str = data.get("profile_image_url", None)
        self.offline_image_url: str = data.get("offline_image_url", None)
        self.created_at: str = data.get("created_at", None)
