from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['start'])
def bot_start(message: Message) -> None:
    """
    Первое сообщение при запуске бота. Установка первоначальных данных пользователя.
    :param message:
    :return:
    """

    user_id = message.from_user.id
    bot.send_message(user_id, f'Привет, {message.from_user.first_name}!')
    bot.send_message(user_id, 'Здесь можно получить информацию с сайта bestchange.ru')
    from .base import base_message
    base_message(user_id)
