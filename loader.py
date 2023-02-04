from telebot import TeleBot
from telebot.types import BotCommand
import config
from services.bestchange import BestChange

bot = TeleBot(token=config.BOT_TOKEN)
bot.set_my_commands([
    BotCommand('start', 'Начало работы')
])
print('START BOT\n', bot.get_me())

best_change = BestChange()
