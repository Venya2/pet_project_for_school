
class DatabaseUtils:
    @staticmethod
    def get_sql_request(foldername: str, filename: str)-> str: 
        with open(f'src/storage/database/sql/{foldername}/{filename}.sql', 'r'
                ) as file:
            table_definition = file.read().strip()
        return table_definition
