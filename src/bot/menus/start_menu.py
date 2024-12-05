
import telebot
from bot.menus.base_menu import BaseMenu
from core.messages.messages_manager import MessagesManager_Json


class StartMenu(BaseMenu):
    def __init__(self):
        ...

    def get_response(self, message: telebot.types.Message):
        print(f'Привет {message.first_name}')
        
