import requests
from toolz import pipe


def request_data(url):
    response = requests.request('GET', url)
    return response.json()

