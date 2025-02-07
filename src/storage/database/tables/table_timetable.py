
import json  
import sqlite3

from get_sql_method import DatabaseUtils
from datetime import datetime
from src.storage.database.core import CoreSQLite
 
class Table_TimeTableSQLite:
    def __init__(self):
        self.db = CoreSQLite.get_connect()

    def c_init(self, input_func):    
        def output_func():
            cursor = self.db.cursor()
            input_func(cursor)
            self.db.commit()
            cursor.close()
        return output_func

    @c_init
    def create_table(self, cursor) -> None :
        cursor.executescript(
            DatabaseUtils.get_sql_request(
                'timetable',
                'create_table'
            )
        )

    @c_init
    def insert_timetable(
        self,
        cursor,
        class_num: int,
        class_letter: str,
        date: datetime, 
        timetable:list[dict]
    ) -> None:
        json_data = json.dumps(timetable)
        cursor.execute(
            DatabaseUtils.get_sql_request(
                'timetable',
                'insert_timetable'
            ),
            (class_num,
            class_letter,
            datetime.strftime(date, '%Y-%m-%d'),
            json_data
            )
        )

    @c_init
    def get_by_id(self, cursor, id: int):
        cursor.execute(DatabaseUtils.get_sql_request(
            'timetable', 'get_by_id'), (id))
        result = cursor.fetchone() 
        if result:  
            retrieved_lesson = json.loads(result[0])
        return retrieved_lesson

    @c_init
    def get_by_date(self, cursor, date: datetime):
        cursor.execute(DatabaseUtils.get_sql_request(
            'timetable', 'get_by_date'), (date))
        result = cursor.fetchone() 
        if result:  
            retrieved_lesson = json.loads(result[0])
        return retrieved_lesson
