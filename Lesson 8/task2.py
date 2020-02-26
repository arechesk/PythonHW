import requests


def get_info(currency):
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{currency}")
    if not response.ok:
        response.raise_for_status()
    data = response.json()
    return data.get("rates")


def convert(quantity, source, target):
    source = source.upper()
    target = target.upper()
    return quantity * get_info(source).get(target)


if __name__ == '__main__':
    print(convert(1, "gbp", "rub"))

