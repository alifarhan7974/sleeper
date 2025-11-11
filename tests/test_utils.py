from api.utils import get
from api.utils import build_url 
from unittest.mock import patch 

import requests 

@patch("api.utils.requests.get")
def test_get(mock_requests_get):
    expected = {"user" : "info"}
    mock_response = mock_requests_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = expected

    url = "https://api.sleeper.app/v1/user/farruali"
    result = get(url)

    assert result == expected 
    mock_requests_get.assert_called_once_with(url)

def test_build_url_basic():
    url = build_url("https://api.sleeper.app", "v1", "user", "farruali")
    assert url == "https://api.sleeper.app/v1/user/farruali"

def test_build_url_with_slash():
    url = build_url("https://api.sleeper.app", "/v1", "/user", "farruali")
    assert url == "https://api.sleeper.app/v1/user/farruali"

def test_build_url_with_int():
    url = build_url("https://api.sleeper.app", "v1", "user", 12345)
    assert url == "https://api.sleeper.app/v1/user/12345"




