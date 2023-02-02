from telebot import TeleBot
from telebot.types import BotCommand
import config


bot = TeleBot(token=config.BOT_TOKEN)
bot.set_my_commands([
    BotCommand('start', 'Начало работы')
])
print('START BOT\n', bot.get_me())
