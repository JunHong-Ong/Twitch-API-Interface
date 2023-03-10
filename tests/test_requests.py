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

    def test_one_id(self):
        """Test requesting with one video id"""

        self.assertRaises(ValueError, next, self.helix.get_videos("notaninteger"))
        self.assertRaises(TypeError, next, self.helix.get_videos(True))
        self.assertRaises(TypeError, next, self.helix.get_videos(123456.0))

    def test_multi_ids(self):
        """Test requesting with multiple video ids"""

        self.assertRaises(ValueError, next, self.helix.get_videos("notaninteger", 123456))
        self.assertRaises(TypeError, next, self.helix.get_videos(True, 123456))
        self.assertRaises(TypeError, next, self.helix.get_videos(123456.0, 123456))


class TestGetChannelById(TestCase):
    """Test cases for getting channel information using broadcaster id"""

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def setUp(self) -> None:
        self.helix = object.__new__(Helix)

    def test_one_id(self):
        """Test requesting with one video id"""

        self.assertRaises(ValueError, next, self.helix.get_channels("notaninteger"))
        self.assertRaises(TypeError, next, self.helix.get_channels(True))
        self.assertRaises(TypeError, next, self.helix.get_channels(123456.0))

    def test_multi_id(self):
        """Test requesting with multiple video ids"""

        self.assertRaises(ValueError, next, self.helix.get_channels("notaninteger", 123456))
        self.assertRaises(TypeError, next, self.helix.get_channels(True, 123456))
        self.assertRaises(TypeError, next, self.helix.get_channels(123456.0, 123456))
