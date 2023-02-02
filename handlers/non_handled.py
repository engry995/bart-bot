from telebot.types import Message
from loader import bot


@bot.message_handler(func=lambda message: True,
                     content_types=['audio', 'photo', 'voice', 'video',
                                    'document', 'text', 'location', 'contact', 'sticker'])
def another_message(message: Message):
    from.base import wrong_message
    wrong_message(message.from_user.id)
