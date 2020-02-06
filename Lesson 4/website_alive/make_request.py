import requests

OK = requests.codes.ok


def request(url):
    r = requests.get(url)
    return r

