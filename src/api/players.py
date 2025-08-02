from api.path_constants import BASE_URL, VERSION, PLAYERS, NFL
from api.utils import build_url, get


def get_players() -> dict: 
    """Makes a get req to https://api.sleeper.app/v1/players/nfl"""
    url = build_url(BASE_URL, VERSION, PLAYERS, NFL)
    return get(url)