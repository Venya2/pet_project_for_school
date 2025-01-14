
import sqlite3

# from database.models.model_user import User
from src.storage.database.core import CoreSQLite



class Table_UsersSQLite:
    def __init__(self):
        self.db = CoreSQLite.get_connect()
        with open('src/storage/database/tables/tables_requests/request_table_users.sql', 'r') as file:  
            self.table_definition = file.read().strip()
        print(self.table_definition)

    def create_table(self):
        cursor = self.db.cursor()
        cursor.executescript(self.table_definition)
        self.db.commit()
        cursor.close()

    def insert_user(self, id: int, username: str, class_num: str, class_letter: str = "а"):
        cursor = self.db.cursor()
        cursor.execute(f"INSERT INTO user VALUES ({id},'{username}', {class_num}, '{class_letter}')")
        self.db.commit()
        cursor.close()

    def get(self, id: int):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM user") 
        response = cursor.fetchall()
        cursor.close()
        return response

    def update_username(self, id: int, new_username: str):
        cursor = self.db.cursor()
        cursor.execute(f"UPDATE user SET username = '{new_username}' WHERE id = {id}") 
        self.db.commit()
        cursor.close()

    def update_class_num(self, id: int, new_class_num: str):
        cursor = self.db.cursor()
        cursor.execute(f"UPDATE user SET class_num = {new_class_num} WHERE id = {id}") 
        self.db.commit()
        cursor.close()

    def update_class_letter(self, id: int, new_class_letter: str = "а"):
        cursor = self.db.cursor()
        cursor.execute(f"UPDATE user SET class_letter = '{new_class_letter}' WHERE id = {id}") 
        self.db.commit()
        cursor.close()


#Проверка
if __name__ == "__main__":
    Table_UsersSQLite().create_table()
#     Table_UsersSQLite().insert_user(321, "kakaxa", 10, "f")
#     print(Table_UsersSQLite().get(321))
#     Table_UsersSQLite().update_class_letter(321, "e")
#     print(Table_UsersSQLite().get(321))
