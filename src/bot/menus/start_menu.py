
import telebot

from src.bot.menus.base_menu import BaseMenu
from src.core.messages.messages_manager import MessagesManager_Json


class StartMenu(BaseMenu):
    def __init__(self, bot: telebot.TeleBot):
        self.bot = bot

    def get_response(self, message: telebot.types.Message):
        self.bot.send_message(
            message.chat.id, f'Привет {message.from_user.first_name}'
        )
        
