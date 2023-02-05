"""
Ключ API бота, и другие ключи должны храниться в файле .env в корневом каталоге проекта.
"""

import os
from dotenv import load_dotenv, find_dotenv

if not (p := find_dotenv()):
    print('Не найден файл .env')
else:
    load_dotenv(dotenv_path=p)

BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    exit('В переменных окружения не найден ключ API телеграмм бота!')

CACHE_TIME = 20  # Время в секундах для кэширования результата, 0 - кэш отключен
NUMBER_RANDOM_POINT_ID = 10  # Количество случайных ID пунктов для выбора
DEBUG = True  # Режим отладки (вывод логов на экран)
