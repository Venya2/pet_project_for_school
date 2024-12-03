
from abc import abstractmethod


class MessagesManager_Base:
    def __init__(self):
        pass

    @abstractmethod
    def get_message(self):
        pass


class MessagesManager_Json(MessagesManager_Base):
    def __init__(self):
        ...

    def get_message(self, field: str):
        """ Здесь должен быть реализован метод, для получения сообщения из файла messages.json """
        ...
