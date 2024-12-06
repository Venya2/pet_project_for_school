""" Здесь будут хэндлеры из телебота, который будут вызывать методы из src.bot.menus """

import telebot

from src.bot.menus.info_menu import InfoMenu
from src.bot.menus.start_menu import StartMenu


class Router:
    def __init__(self, bot: telebot.TeleBot):
        self.bot = bot
        self.routers_commands()
        self.routers_buttons()

    def routers_commands(self):

        @self.bot.message_handler(commands=["start"])
        def start(message: telebot.types.Message):
            return StartMenu(self.bot).get_response(message)
        
        @self.bot.message_handler(commands=["info"])
        def info(message: telebot.types.Message):
            return InfoMenu(self.bot).get_response(message)
        

    def routers_buttons(self):
        ...
