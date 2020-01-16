import pytest
from unittest.mock import patch
from unittest.mock import MagicMock
from lab_11.tasks.tools.metaweather import get_metaweather, get_cities_woeid
import requests


def test_get_cities_woeid():
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {"title": "Warsaw", "woeid": 523920},
        {"title": "Newark", "woeid": 2459269},
    ]
    mock_response.status = 200

    with patch("requests.get", return_value=mock_response) as mock_func:
        assert get_cities_woeid("War") == {
            "Warsaw": 523920,
            "Newark": 2459269,
        }
    print("\n" + str(mock_response.json.call_count))


def test_get_cities_raises_timeout():

    with patch("requests.get", side_effect=requests.exceptions.Timeout()) as mock_func:
        with pytest.raises(requests.exceptions.Timeout):
            get_cities_woeid("Warszawa", 0.1)
