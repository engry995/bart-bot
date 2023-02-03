from telebot.types import Message


def listener(message) -> None:
    """
    Функция выводит все сообщения пользователей на экран.
    :param message: Сообщение из телеграмм.
    :return: None
    """

    if message:
        message = message[0]
        print(f'Сообщение id={message.id} от {message.from_user.full_name}, user_id={message.from_user.id}: {message.text}')
    else:
        print('Получен пустой список.')
