import requests
from urllib.parse import urljoin


def get_cities_woeid(query: str, timeout: float = 5.):
    API_URL = 'https://www.metaweather.com/api/'
    location_url = urljoin(API_URL, 'location/search')
    response_dictionary = {}

    try:
        response = requests.get(location_url, params=dict(query=query), timeout=timeout)
    except requests.exceptions.Timeout:
        print(f'Request for: {location_url} took to long!')
    else:
        if response.status_code >= 400:
            raise requests.exceptions.HTTPError

        try:
            cities = response.json()
        except RuntimeError:
            print('Runtime Error')

        for city in cities:
            response_dictionary[city['title']] = city['woeid']
    finally:
        return response_dictionary


if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)


