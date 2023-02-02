from typing import Union
import requests
from bs4 import BeautifulSoup


class BestChange:

    POINT_NOT_EXIST = -111
    NOT_RESPONSE = -222

    def __init__(self, point_id: Union[str, int]):

        if isinstance(point_id, int) or point_id.isdigit():
            self.point_id = point_id
        else:
            raise TypeError('point_id may be int or string of digit')
        self.base_url = 'https://www.bestchange.ru/'

    @property
    def difference_with_first_by_btc_usdt(self) -> float:
        url_suffix = 'bitcoin-to-tether-trc20.html'
        return self.__get_difference_between_first(url_suffix)

    def __get_difference_between_first(self, url_suffix: str) -> float:
        url = self.base_url + url_suffix
        data = self.get_parsed_data(url)
        return data

    def get_parsed_data(self, url):
        data = self.get_raw_html(url)
        if data == self.NOT_RESPONSE:
            return data
        data = self.parse_rate(data)
        return data

    def get_raw_html(self, url: str) -> Union[str, int]:
        for i in range(3):
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    reply = response.text
                    break
            except requests.exceptions.RequestException:
                pass
        else:
            reply = self.NOT_RESPONSE
        return reply

    def parse_rate(self, html_data: str) -> dict:
        data = BeautifulSoup(html_data)
        print(html_data)
        result = {}
        result = 5556
        return result