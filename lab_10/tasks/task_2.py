import pathlib
from typing import Optional, Union, List
from urllib.parse import urljoin
import requests
import os
import csv

API_URL = "https://www.metaweather.com/api/"


def get_city_data(
    woeid: int,
    year: int,
    month: int,
    path: Optional[Union[str, pathlib.Path]] = None,
    timeout: float = 5.0,
) -> (str, List[str]):
    _path = pathlib.Path.cwd()
    if type(path) == pathlib.PosixPath:
        save_path = path
    elif type(path) == str:
        save_path = pathlib.PosixPath(path) / f"{woeid}_{year}_{month:02}"
    else:
        save_path = _path / f"{woeid}_{year}_{month:02}"
    if not os.path.exists(os.path.dirname(str(save_path) + "/")):
        try:
            os.makedirs(os.path.dirname(str(save_path) + "/"))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    session = requests.session()
    stored_files = []
    for day in range(1, 32):
        location_url = urljoin(API_URL, f"location/{woeid}/{year}/{month}/{day}")
        response = session.get(location_url, timeout=timeout)
        if response.json():
            with open(save_path / f"{year}_{month:02}_{day:02}.csv", mode="w+") as f:
                writer = csv.writer(
                    f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
                )
                first_row = True
                for row in response.json():
                    if first_row:
                        first_row = False
                        writer.writerow(row.keys())
                    writer.writerow(row.values())
                stored_files.append(save_path / str(day))
    return str(save_path), stored_files


if __name__ == "__main__":
    _path = pathlib.Path.cwd()
    expected_path = _path / "523920_2017_03"
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = "weather_data/523920_2017_03"
    dir_path, file_paths = get_city_data(523920, 2017, 3, path="weather_data")
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = "weather_data/523920_2012_12"
    dir_path, file_paths = get_city_data(523920, 2012, 12, path="weather_data")
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path
