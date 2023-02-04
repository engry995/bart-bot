from telebot.types import Message
from loader import bot
from services.bestchange import BestChange

best_change = BestChange()


def base_message(user_id: int):
    bot.send_message(user_id, 'Введите ID обменного пункта:')


def wrong_message(user_id: int):
    bot.send_message(user_id, 'Нужно ввести целое число!')
    base_message(user_id)


def message_from_bestchange(user_id, point_id):

    reply = best_change.difference_with_first_by_btc_usdt(point_id)

    if reply == BestChange.POINT_NOT_EXIST:
        reply = f'Информация по пункту с ID <{point_id}> не найдена.'
    elif reply == BestChange.NOT_RESPONSE:
        reply = f'Нет ответа от {best_change.base_url}. Попробуйте позже.'

    bot.send_message(user_id, reply)
    base_message(user_id)


@bot.message_handler(content_types=['text'])
def main_handler(message: Message):
    user_id = message.from_user.id
    text = message.text.strip()
    if text.isdigit():
        message_from_bestchange(user_id, text)
    else:
        wrong_message(user_id)
