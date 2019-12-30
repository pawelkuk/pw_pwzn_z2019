import requests
from urllib.parse import urljoin
from typing import Dict

API_URL = "https://www.metaweather.com/api/"


def get_cities_woeid(query: str, timeout: float = 5.0) -> Dict[str, int]:
    location_url = urljoin(API_URL, "location/search")
    params = {"query": query}
    response = requests.get(location_url, params=params, timeout=timeout)

    return {doc["title"]: doc["woeid"] for doc in response.json()}


if __name__ == "__main__":
    assert get_cities_woeid("Warszawa") == {}
    assert get_cities_woeid("War") == {"Warsaw": 523920, "Newark": 2459269}
    try:
        get_cities_woeid("Warszawa", 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
