import json
from unittest import TestCase
from unittest.mock import patch
import math
import random

from twitch.helix import Helix

HELIX_DATA = {}

def setUpModule():
    """Load Helix responses needed for tests"""
    global HELIX_DATA
    with open('tests/fixtures/helix_responses.json', encoding='utf-8') as json_data:
        HELIX_DATA = json.load(json_data)

def _generate_response(method, url, headers, params, json, timeout):
    print(method, url, headers, params, json, timeout)
    return

class TestGetVideoById(TestCase):
    """Test cases for getting video information using video id"""

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def setUp(self) -> None:
        self.helix = object.__new__(Helix)

    async def test_one_id(self):
        """Test requesting with one video id"""

        with self.assertRaises(ValueError):
            await self.helix.videos("notaninteger")
        with self.assertRaises(TypeError):
            await self.helix.videos(True)
        with self.assertRaises(TypeError):
            await self.helix.videos(123456.0)

    async def test_multi_ids(self):
        """Test requesting with multiple video ids"""

        with self.assertRaises(ValueError):
            await self.helix.videos("notaninteger", 123456)
        with self.assertRaises(TypeError):
            await self.helix.videos(True, 123456)
        with self.assertRaises(TypeError):
            await self.helix.videos(123456.0, 123456)
