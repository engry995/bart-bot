import config
from loader import bot
from services.utils import listener
import handlers


if __name__ == '__main__':

    if config.DEBUG:
        print('DEBUG MODE')
        bot.set_update_listener(listener)
    bot.infinity_polling()
