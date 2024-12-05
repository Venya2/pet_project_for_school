""" Здесь будут хэндлеры из телебота, который будут вызывать методы из src.bot.menus """

import telebot
from bot.menus.start_menu import StartMenu

class Router:
    def __init__(self, bot):
        self.bot = bot
        self.routers_commands()
        self.routers_buttons()

    def routers_commands(self):

        @self.bot.message_handler(commands=["start"])
        def start(message: telebot.types.Message):
            return StartMenu().get_response(message)

    def routers_buttons(self):
        ...
