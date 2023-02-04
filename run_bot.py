import logging
from telebot import logger
import config
from loader import bot
from services.utils import listener
import handlers


if __name__ == '__main__':

    logger_level = None
    if config.DEBUG:
        logger.setLevel(logging.INFO)
        logger.info('DEBUG MODE')
        bot.set_update_listener(listener)
        logger_level = logging.INFO

    bot.infinity_polling(logger_level=logger_level)
