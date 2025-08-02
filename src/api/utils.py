import requests 
from typing import Any


def get(url: str) -> Any: 
    """Wrapper for get method"""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def build_url(base_url: str, *paths: str | int) -> str: 
    """Builds full url. Okay if path is not int or doesn't start with /. """
    full_url = base_url 
    for path in paths: 
        path = str(path)
        if path.startswith("/"):
            full_url += str(path)
        else: 
            full_url += "/" + str(path) 
    print(full_url)
    return full_url








