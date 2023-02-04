from telebot.types import Message, CallbackQuery
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import logger
from loader import bot, best_change
from services.bestchange import BestChange


def base_message(user_id: int):

    points = best_change.get_random_point_by_btc_usdt()
    markup = InlineKeyboardMarkup(row_width=5)
    markup.add(*[InlineKeyboardButton(text=point, callback_data=f'point_id:{point}') for point in points])

    bot.send_message(user_id, 'Введите ID обменного пункта или выберите из предложенных:', reply_markup=markup)


def wrong_message(user_id: int):
    bot.send_message(user_id, 'Нужно ввести целое число!')
    base_message(user_id)


def message_from_bestchange(user_id, point_id):

    reply = best_change.difference_with_first_by_btc_usdt(point_id)
    if reply == BestChange.POINT_NOT_EXIST:
        reply = f'Информация по пункту с ID <{point_id}> не найдена.'
    elif reply == BestChange.NOT_RESPONSE:
        reply = f'Нет ответа от {best_change.base_url}. Попробуйте позже.'
    elif reply == BestChange.PARSING_FAIL:
        reply = 'Сбой обработки. Попробуйте позже.'

    bot.send_message(user_id, reply)
    logger.info(f'Отправлено сообщение для {user_id} ::: {reply}')
    base_message(user_id)


@bot.message_handler(content_types=['text'])
def main_handler(message: Message):
    user_id = message.from_user.id
    text = message.text.strip()
    if text.isdigit():
        message_from_bestchange(user_id, text)
    else:
        wrong_message(user_id)


@bot.callback_query_handler(func=lambda call: call.data.startswith('point_id:'))
def callback_point_id(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    point_id = call.data.replace('point_id:', '')
    message_from_bestchange(user_id, point_id)
