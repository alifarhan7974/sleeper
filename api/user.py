from api.path_constants import BASE_URL, VERSION, USER
from api.utils import get, build_url


def get_user(username: str) -> dict: 
    """Makes API call to https://api.sleeper.app/v1/user/<username>"""

    url = build_url(BASE_URL, VERSION, USER, username)
    return get(url)