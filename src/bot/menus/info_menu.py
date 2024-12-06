
import telebot


class InfoMenu:
    def __init__(self, bot: telebot.TeleBot):
        self.bot = bot

    def get_response(self, message: telebot.types.Message):
        self.bot.send_message(
            message.chat.id,
            'Этот бот сделан для получения расписания и домашнего задания. Чтобы домашнее задание' +\
            ' тут появлялось, нужно чтоб его кто-то сюда присылал. Это могут сделать ваши одноклассники или Вы'
        )
