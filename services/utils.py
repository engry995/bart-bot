from telebot.types import Message
from telebot import logger


def listener(message: list[Message]) -> None:
    """
    Функция выводит все сообщения пользователей на экран.
    :param message: Сообщение из телеграмм.
    :return: None
    """

    if message:
        message = message[0]
        logger.info(f'Сообщение id={message.id} от {message.from_user.full_name}, '
                    f'user_id={message.from_user.id}: {message.text}')
    else:
        logger.info('Получен пустой список.')
