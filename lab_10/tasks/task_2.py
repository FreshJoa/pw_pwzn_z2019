import csv
import pathlib
from typing import Optional, Union, List
from calendar import monthrange
from urllib.parse import urljoin
import requests

API_URL = 'https://www.metaweather.com/api/'


def get_data(woeid, year, month, day, timeout):
    location_url = urljoin(API_URL, f'location/{woeid}/{year}/{month}/{day}')
    try:
        response = requests.get(location_url, timeout=timeout)
    except requests.exceptions.Timeout:
        print(f'Request for: {location_url} took to long!')
    else:
        if response.status_code >= 400:
            raise requests.exceptions.HTTPError

        try:
            data = response.json()
        except RuntimeError:
            print('Runtime Error')
    finally:
        return data


def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.
) -> (str, List[str]):
    if path is None:
        path = pathlib.Path.cwd()
    else:
        path = pathlib.Path(path)
    finally_path = path / f'{woeid}_{year}_{month:02d}'
    finally_path.mkdir(parents=True, exist_ok=True)
    days_in_month = monthrange(year, month)[1]
    paths_list = []

    for day in range(1, days_in_month + 1):
        data = get_data(woeid, year, month, day, timeout)
        if data:
            file_name = f'{year}_{month:02d}_{day:02d}.csv'
            with open(finally_path / file_name, 'w') as _file:
                writer = csv.DictWriter(_file, delimiter=',', quotechar='"', fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            paths_list.append(file_name)

    return str(finally_path), paths_list


if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = 'weather_data/523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = 'weather_data/523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path
