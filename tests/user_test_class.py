from api.user import get_user
from unittest import TestCase
import requests 

class MockResponse: 

    def __init__(self, status_code=200): 
        self.status_code = status_code 

    def raise_for_status(self): 
        if self.status_code != 200: 
            raise Exception("Return Code was not 200")

    def json(self): 
        return {"Username" : "info"}

def mock_get(*args, **kwargs):
    return MockResponse() 

def mock_get1(*args, **kwargs): 
    return MockResponse(404)

class TestUser(TestCase): 

    def test_get_user(self):
        requests.get = mock_get

        info = get_user("farruali")
        assert info ==  {"Username" : "info"}
        
    def test_exceptions(self): 
        requests.get = mock_get
        try: 
            response = get_user("farruali")
            print(response)
            self.assertFalse(True)  
        except Exception as e: 
            print(e)
            self.assertTrue(False) 
