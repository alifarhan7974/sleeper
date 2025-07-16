from path_constants import BASE_URL, VERSION, USER
from utils import get, build_url



def get_user(username: str) -> str: 
    """Makes API call to https://api.sleeper.app/v1/user/<username>"""

    username = "/" + username 
    url = build_url(BASE_URL, VERSION, USER, username)
    return get(url)