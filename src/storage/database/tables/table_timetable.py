
from abc import abstractmethod

from storage.database.core import CoreSQLite


class Table_TimeTableBase:
    def __init__(self):
        pass

    @abstractmethod
    def create(self, id):
        pass


class Table_TimeTableSQLite(Table_TimeTableBase):
    def __init__(self):
        ...

    def create(self, id):
        ...

