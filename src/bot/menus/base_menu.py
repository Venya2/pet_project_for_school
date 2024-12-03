
from abc import abstractmethod


class BaseMenu:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_response(self):
        """ Здесь будет реализован метод, который работает с ui """
        ...
