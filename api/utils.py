import requests 
from typing import Any


def get(url: str) -> Any: 
    print(url)
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def build_url(base_url: str, *paths: str | int) -> str: 
    full_url = base_url 
    for path in paths: 
        full_url += str(path)
    
    return full_url








