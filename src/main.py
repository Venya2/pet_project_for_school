
import telebot

from src.core.config import settings
from src.bot.routers import Router


class Main:
    def __init__(self):
        self.bot = telebot.TeleBot(settings.token)
        Router(self.bot)


    def start(self):
        self.bot.polling(none_stop=True)

if __name__ == "__main__":
    Main().start()
