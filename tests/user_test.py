
from api.user import get_user
from unittest.mock import patch


@patch("api.user.get")
def test_get_user(mock_get):
    expected = {"user" : "info"}
    mock_get.return_value = expected

    result = get_user("farruali")

    # If called with is correct, build url also worked 
    mock_get.assert_called_once_with("https://api.sleeper.app/v1/user/farruali")
    assert result == expected 
    

"""
@patch("requests.get")
def test_get_user(mock_get):
    answer = {"User" : "Info"}
    response = mock_get.return_value
    response.status_code = 200 
    response.json.return_value = answer
    result = get_user("farruali") 
    assert result == answer 



@patch("requests.get")
def test_get_user_exception(mock_get):
    answer = {"User" : "Info"}
    response = mock_get.return_value
    response.status_code = 401 
    response.json.return_value = answer
    
    result = get_user("farruali") 
    assert result == answer 
    pass

def test_exceptions(): 
    pass
"""
