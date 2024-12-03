
from abc import abstractmethod

from database.core import CoreBase
from database.models.model_user import User


class Table_UsersBase:
    def __init__(self):
        pass

    @abstractmethod
    def create(self, id: int):
        """
        Метод нужен для создания пользователя в базе данных
        """
        pass

    @abstractmethod
    def get(self, id: int) -> User:
        """
        Метод нужен для получения пользователя из базы данных
        """
        pass


class Table_UsersSQLite(Table_UsersBase):
    def __init__(self):
        ...

    def create(self, id: int):
        ...

    def get(self, id: int) -> User:
        ...    
