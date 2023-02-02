from telebot.types import Message
from loader import bot
from services.bestchange import get_difference_between_first_by_btc_usdt


def base_message(user_id: int):
    bot.send_message(user_id, 'Введите ID обменного пункта:')


def wrong_message(user_id: int):
    bot.send_message(user_id, 'Нужно ввести целое число!')
    base_message(user_id)


def message_about_rate_difference(user_id, text):
    reply = get_difference_between_first_by_btc_usdt(text)
    bot.send_message(user_id, f'MESSAGE: {text}\nREPLY: {reply}')


@bot.message_handler(content_types=['text'])
def main_handler(message: Message):
    user_id = message.from_user.id
    text = message.text.strip()
    if text.isdigit():
        message_about_rate_difference(user_id, text)
    else:
        wrong_message(user_id)

@bot.message_handler
def another_message(message: Message):
    wrong_message(message.from_user.id)
