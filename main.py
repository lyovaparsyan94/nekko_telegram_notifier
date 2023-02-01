from config.constants import *
from config.config_loader import ConfigLoader
from telegram_notifier import *

token = ConfigLoader.config_loader(config_file=CONFIG_FILE)['arm_bot_token']

if __name__ == '__main__':
    bot.infinity_polling()
