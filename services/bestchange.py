import requests

def get_difference_between_first_by_btc_usdt(point_id: str) -> float:
    url = 'https://www.bestchange.ru/bitcoin-to-tether-trc20.html'
    return get_difference_between_first(point_id, url)


def get_difference_between_first(point_is: str, url: str) -> float:
    data = get_parsed_data(url)
    return data


def get_parsed_data(url: str):
    response = requests.get(url)
    print(response.text)

    return 797.5
