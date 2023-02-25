import json
from requests import Response
from unittest import TestCase
from unittest.mock import patch, Mock

from twitch.interface import HelixInterface, Token

HELIX_DATA = {}

def setUpModule():
    """Load Helix responses needed for tests"""
    global HELIX_DATA
    with open('tests/fixtures/helix_token_response.json') as json_data:
        HELIX_DATA = json.load(json_data)

class TestAuthorization(TestCase):
    """Test cases for requesting an app access token for authorization"""
    
    ######################################################################
    #  T E S T   C A S E S
    ######################################################################    

    @patch('requests.request')
    def test_valid_credentials(self, interface_mock):
        """Test getting an app access token with valid credentials"""
        
        interface_mock.return_value = Mock(spec=Response,
                                           status_code=200)
        interface_mock.return_value.json.return_value = HELIX_DATA["TOKEN"]["GOOD_REQUEST"]

        interface = HelixInterface("test_id", "test_secret")
        self.assertIsNotNone(interface.token)
        self.assertIsInstance(interface.token, Token)
        self.assertEqual(interface.token.value, "jostpf5q0uzmxmkba9iyug38kjtgh")
        self.assertEqual(str(interface.token), "Bearer jostpf5q0uzmxmkba9iyug38kjtgh")
    
    @patch('requests.request')
    def test_invalid_client_id(self, interface_mock):
        """Test getting an app access token with invalid client id"""
        
        interface_mock.return_value = Mock(spec=Response,
                                           status_code=400)
        interface_mock.return_value.json.return_value = HELIX_DATA["TOKEN"]["INVALID_ID"]

        with self.assertRaises(ValueError) as cm:
            HelixInterface("test_id", "test_secret")
        
        self.assertEqual(str(cm.exception), "invalid client")
    
    @patch('requests.request')
    def test_invalid_client_secret(self, interface_mock):
        """Test getting an app access token with invalid client secret"""
        
        interface_mock.return_value = Mock(spec=Response,
                                           status_code=403)
        interface_mock.return_value.json.return_value = HELIX_DATA["TOKEN"]["INVALID_SECRET"]

        with self.assertRaises(ValueError) as cm:
            HelixInterface("test_id", "test_secret")
        
        self.assertEqual(str(cm.exception), "invalid client secret")

    @patch('requests.request')
    def test_invalid_grant_type(self, interface_mock):
        """Test getting an app access token with invalid grant type"""
        
        interface_mock.return_value = Mock(spec=Response,
                                           status_code=400)
        interface_mock.return_value.json.return_value = HELIX_DATA["TOKEN"]["INVALID_GRANT_TYPE"]

        with self.assertRaises(ValueError) as cm:
            HelixInterface("test_id", "test_secret")
        
        self.assertEqual(str(cm.exception), "invalid grant type")