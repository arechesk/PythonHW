import requests


def get_size(url):
    response = requests.get(url)
    if not response.ok:
        raise response.raise_for_status()
    return len(response.text)


if __name__ == '__main__':
    print(f"size google.com: {get_size('https://google.com')}")