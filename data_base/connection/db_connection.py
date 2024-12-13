import sqlite3

from file_work.path_validator.path_validator import PathValidator
from file_work.utils.utilities import Check
from ..utils.utilities import Messages

class DatabaseConnection:
    def __init__(self, path_params):
        self.path_params = path_params
        self.db_path = None
        self.connection = None
        self.extract_db_path()

    def connect(self):
        if not PathValidator.for_read(self.path_params.get('folder_path', ''),
                                      self.path_params.get('file_name', ''),
                                      self.path_params.get('extension', ''),
                                      ['db']):
            Messages.Error.connection(self.db_path)
            return

        try:
            self.connection = sqlite3.connect(self.db_path)
        except Exception as e:
            Messages.Error.try_action(e)
            return

        Messages.Complete.connection(self.db_path)

    def create_db(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
        except Exception as e:
            Messages.Error.try_action(e)
            return

        Messages.Complete.connection(self.db_path)

    def close(self):
        if self.connection:
            self.connection.close()
            Messages.Complete.close_connection(self.db_path)
        else:
            Messages.Error.miss_connection(self.db_path)

    def extract_db_path(self):
        specified_keys = ["folder_path", "file_name", "extension"]

        if not Check.dictionary_specified(self.path_params, specified_keys):
            Messages.Error.specified_dictionary(specified_keys)
            return None

        folder_path = self.path_params.get('folder_path', '')
        file_name = self.path_params.get('file_name', '')
        extension = self.path_params.get('extension', '')

        self.db_path = PathValidator.get_full_path(folder_path, file_name, extension)
