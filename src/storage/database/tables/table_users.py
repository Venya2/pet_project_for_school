
import sqlite3
from get_sql_method import DatabaseUtils

from src.storage.database.core import CoreSQLite



class Table_UsersSQLite:
    def __init__(self):
        self.db = CoreSQLite.get_connect()

    def c_init(self, input_func):    
        def output_func():
            cursor = self.db.cursor()
            input_func(cursor)
            self.db.commit()
            cursor.close()
        return output_func

    def create_table(self, cursor) -> None :
        cursor.executescript(DatabaseUtils.get_sql_request('users', 'create_table'))

    @c_init
    def insert_user(
        self,
        cursor,
        id: int,
        username: str,
        class_num: str,
        class_letter: str = "а"
        ) -> None:
        cursor.execute(DatabaseUtils.get_sql_request(
            'users', 'insert_user'), (id, username, class_num, class_letter))

    @c_init
    def get(self, cursor, id: int):
        cursor.execute(DatabaseUtils.get_sql_request('users', 'get'))
        response = cursor.fetchall()
        return response

    @c_init
    def update_username(
        self,
        cursor,
        id: int,
        new_username: str
        ) -> None:
        cursor.execute(DatabaseUtils.get_sql_request('users', 'update_username'), (new_username, id))

    @c_init
    def update_class_num(
        self,
        cursor,
        id: int,
        new_class_num: str
        )-> None:
        cursor.execute(
            DatabaseUtils.get_sql_request('users', 'update_class_num'), (new_class_num, id))

    @c_init
    def update_class_letter(
        self,
        cursor,
        id: int,
        new_class_letter: str = "а"
        ) -> None :
        cursor.execute(DatabaseUtils.get_sql_request(
            'users', 'update_class_letter'), (new_class_letter, id)) 
