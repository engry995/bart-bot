from typing import Union, Optional
from time import time
import random
import re
from bs4.element import Tag
import requests
from bs4 import BeautifulSoup
import config
from telebot import logger

class BestChange:

    POINT_NOT_EXIST = -111
    NOT_RESPONSE = -222
    PARSING_FAIL = -333

    __cache_data_btc_usd = None
    __time_cache_btc_usd = 0

    def __init__(self):

        self.base_url = 'https://www.bestchange.ru/'
        self.url_suffix_btc_usd = 'bitcoin-to-tether-trc20.html'
        self.error_occurred = False
        self.error = None

    @classmethod
    def __get_table_from_cache(cls) -> Optional[dict]:
        now = time()
        if now - cls.__time_cache_btc_usd <= config.CACHE_TIME:
            logger.info('Получили данные из кэша')
            return cls.__cache_data_btc_usd

    @classmethod
    def __write_table_to_cache(cls, table: dict) -> None:
        cls.__cache_data_btc_usd = table
        cls.__time_cache_btc_usd = time()
        logger.info('Записали данные в кэш')

    def __reset_error(self):
        self.error_occurred = False
        self.error = None

    def difference_with_first_by_btc_usdt(self, point_id: Union[str, int]) -> float:
        url_suffix = self.url_suffix_btc_usd
        reply = self.__get_difference_between_first(url_suffix, point_id)
        if self.error_occurred:
            return self.error
        else:
            return reply

    def get_random_point_by_btc_usdt(self, count=10) -> list[str]:
        self.__reset_error()
        data = self.get_parsed_data(self.base_url + self.url_suffix_btc_usd)
        points = [point for point in data.keys() if point and point.isdigit()]
        return random.sample(points, count)

    def __get_difference_between_first(self, url_suffix: str, point_id: Union[str, int]) -> Optional[float]:

        if isinstance(point_id, int):
            point_id = str(point_id)
        elif not isinstance(point_id, str) or not point_id.isdigit():
            raise TypeError('point_id may be int or string of digit')

        url = self.base_url + url_suffix

        self.__reset_error()
        data = self.get_parsed_data(url)
        if self.error_occurred:
            return

        point_rate = data.get(point_id)
        if not point_rate:
            self.error_occurred = True
            self.error = self.POINT_NOT_EXIST
            point_rate = 0
        return data['first_line'] - point_rate

    def get_parsed_data(self, url):
        data = self.__get_table_from_cache()
        if data:
            return data

        data = self.get_raw_html(url)
        if self.error_occurred:
            return
        data = self.parse_rate(data)
        return data

    def get_raw_html(self, url: str) -> Optional[str]:
        logger.info('Получаем данные с сервера')
        reply = None
        for i in range(3):
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    reply = response.text
                    break
            except requests.exceptions.RequestException:
                pass
        else:
            self.error_occurred = True
            self.error = self.NOT_RESPONSE
        return reply

    def parse_rate(self, html_data: str) -> Optional[dict]:
        data = BeautifulSoup(html_data, features='html.parser')
        rate_table = data.find(id='rates_block').tbody.contents
        result = {}
        for line in rate_table:
            id_point, rate = self.__parse_table_line(line)
            result[id_point] = rate
        if len(result) == 0:
            self.error_occurred = True
            self.error = self.PARSING_FAIL
            return
        result['first_line'] = self.__get_first_line_rate(rate_table)
        self.__write_table_to_cache(result)
        return result

    @staticmethod
    def __parse_table_line(line: Tag):

        point_id, rate = None, None
        if not isinstance(line, Tag):
            return point_id, rate

        try:
            url_to_point = line.find(class_='bj').a.get('href')
            point_id = re.search(r'(?<=id=)\d+', url_to_point)
            rate = line.find_all(class_='bi')[1]
            rate = rate.next_element

            if point_id and rate:
                point_id = point_id.group()
                rate = str(rate.string)
                rate = float(rate.strip().replace(' ', ''))

        except (TypeError, AttributeError, IndexError, ValueError):
            point_id, rate = None, None

        return point_id, rate

    def __get_first_line_rate(self, table):
        for line in table:
            _, rate = self.__parse_table_line(line)
            if rate:
                return rate
