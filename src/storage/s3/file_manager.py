
from abc import abstractmethod


class FileManagerBase:
    def __init__(self):
        pass

    @abstractmethod
    def upload_file(self, file_name: str):
        """
        Метод нужен, для загрузки файла в S3 хранилище
        """
        pass

    @abstractmethod
    def get_file(self, file_name: str):
        """
        Метод нужен, для скачивания файла с S3 хранилища
        """
        pass
