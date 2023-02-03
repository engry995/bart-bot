"""
Ключ API бота, и другие ключи должны храниться в файле .env в корневом каталоге проекта.
"""

import os
from dotenv import load_dotenv, find_dotenv

if not (p := find_dotenv()):
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv(dotenv_path=p)

BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    print('В переменных окружения не найден ключ API телеграмм бота!')

CACHE_TIME = 20  # Время в секундах для кэширования результата, 0 - кэш отключен
DEBUG = True
