import json
import random
from unittest import TestCase
from unittest.mock import patch, Mock
from requests import Response

from twitch.helix import Helix
from twitch.interface import HelixInterface, Token

HELIX_DATA = {}

def setUpModule():
    """Load Helix responses needed for tests"""
    global HELIX_DATA
    with open('tests/fixtures/helix_responses.json', encoding='utf-8') as json_data:
        HELIX_DATA = json.load(json_data)

class TestGetVideoById(TestCase):
    """Test cases for getting video information using video id"""

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def setUp(self) -> None:
        self.helix = object.__new__(Helix)
        self.BASE_URL = "https://api.twitch.tv/helix/videos"

    def test_one_id(self):
        """Test requesting with one video id"""

        self.assertRaises(ValueError, self.helix.get_videos, "notaninteger")
        self.assertRaises(TypeError, self.helix.get_videos, True)
        self.assertRaises(TypeError, self.helix.get_videos, 123456.0)

    def test_multi_id(self):
        """Test requesting with multiple video ids"""

        self.assertRaises(ValueError, self.helix.get_videos, "notaninteger", 123456)
        self.assertRaises(TypeError, self.helix.get_videos, True, 123456)
        self.assertRaises(TypeError, self.helix.get_videos, 123456.0, 123456)
