Телеграмм бот для работы с курсами валют на bestchange.ru
=========================================================

Бот предназначен для получения разницы курса валюты с лучшим курсом.

Реализованные функции
---------------------

* Вывод разницы курса валюты заданного обменного пункта с лучшим курсом.
* Подсказка, если введенный ID не соответствует формату
* Инлайн-клавиатура, с возможностью выбора ID пункта из нескольких случайных.
* Кэширование результатов запроса на определенное время
* Логирование в режиме отладки
* создан Docker образ для быстрого запуска

**_Данные получаются с сайта [bestchange.ru]() по валютной паре BTC-USDT_**  
_[https://www.bestchange.ru/bitcoin-to-tether-trc20.html]()_

Инструкция по установке и первому запуску 
-----------------------------------------

### Запуск из Docker образа
1. Необходим установленный Docker в системе  
[Инструкция по установке](https://docs.docker.com/get-docker/)  
2. Выполнить команду для загрузки образа
```commandline
docker pull engry995/bart-bot
```
3. Запустить образ
```commandline
docker run -e BOT_TOKEN=TOKEN_TELEGRAMM_BOT engry995/bart-bot
```
где *TOKEN_TELEGRAMM_BOT* - токен, полученный от API телеграмм при создании бота  
[Страница на DockerHub](https://hub.docker.com/r/engry995/bart-bot)

### Запуск из исходных файлов

1. Скопировать файлы проекта
```commandline
git clone https://github.com/engry995/bart-bot.git
```
Эта команда создаст папку `bart-bot`  и сохранит в ней все требуемые файлы.

2. Установить зависимости:
```commandline
pip install -r requirements.txt
```
*Рекомендуется настроить [виртуальное окружение](https://docs.python.org/3/library/venv.html).*

3. Создать нового бота и получить токен для работы с ним.  
    1. В приложении telegramm нужно отправить сообщение боту [BotFather](https://t.me/botfather)
    2. Создать нового бота командой `/newbot`
    3. Выполнить несколько простых шагов  
[Руководство](https://core.telegram.org/bots#how-do-i-create-a-bot) 

5. Переименовать файл `.env.template` в `.env`, указать в нем свой токен для бота  
Пример файла `.env`:
```dotenv
BOT_TOKEN='5129698927:AAGDrtF8BhpsZkfJkz8d8V8sd80--------'
```

6. Запустить программу
```commandline
python run_bot.py
```

Работа с телеграмм ботом
------------------------
### Начало работы
Для начала работы отправьте боту команду `/start`

### Получение информации
   * Отравить сообщение боту с ID обменного пункта (*ID пункта - целое число*)
   * Или выбрать из случайно выбранных ID пунктов, по которым есть информация  
   
   В ответ придет число - разница между курсом выбранного пункта и курсом в первой строке таблицы.

Настройки бота
--------------

В файле `config.py` находятся настройки, регулирующие поведение бота.

```dotenv
CACHE_TIME = 20  # Время в секундах для кэширования результата, 0 - кэш отключен
NUMBER_RANDOM_POINT_ID = 10  # Количество случайных ID пунктов для выбора
DEBUG = True  # Режим отладки (вывод логов на экран)

```
