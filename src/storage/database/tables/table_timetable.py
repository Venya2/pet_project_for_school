import json  
import sqlite3
# import tables_requests
from datetime import datetime
from src.storage.database.core import CoreSQLite

class Table_TimeTableSQLite:
    def __init__(self):
        self.db = CoreSQLite.get_connect()


    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS timetable (
            id INTEGER PRIMARY KEY,
            class_num INT,
            class_letter TEXT,
            date DATE,
            timetable TEXT
        )''')
        self.db.commit()
        cursor.close()

    def insert_timetable(self, class_num: int, class_letter: str, date: datetime, timetable: list[dict]):
        cursor = self.db.cursor()
        json_data = json.dumps(timetable)
        cursor.execute("INSERT INTO timetable (class_num, class_letter, date, timetable) VALUES (?, ?, ?, ?)",  
               (class_num, class_letter, datetime.strftime(date, '%Y-%m-%d'), json_data))
        self.db.commit()
        cursor.close()

    def get_by_id(self, id: int):
        cursor = self.db.cursor()
        cursor.execute(f"SELECT * FROM timetable WHERE id = {id}")
        result = cursor.fetchone() 
        if result:  
            retrieved_lesson = json.loads(result[0])
        cursor.close()
        return retrieved_lesson

    def get_by_date(self, date: datetime):
        cursor = self.db.cursor()
        cursor.execute(f"SELECT * FROM timetable WHERE date = {date}")
        result = cursor.fetchone() 
        if result:  
            retrieved_lesson = json.loads(result[0])
        cursor.close()
        return retrieved_lesson
    
# Проверка
# if __name__ == "__main__":
#     Table_TimeTableSQLite().create_table()
#     timestamp_str = '2024-12-20'  
#     timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d')  
#     Table_TimeTableSQLite().insert_timetable(10, "g", timestamp, ['GEAR'])

# print(Table_TimeTableSQLite())
# print(Table_TimeTableSQLite())