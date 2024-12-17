import os
import sqlite3

from file_work.path_validator.path_validator import PathValidator
from ..utils.utilities import Messages

class DatabaseConnection:
    def __init__(self, path_params):
        self.path_params = path_params
        self.db_path = None
        self.connection = None

        self.extract_db_path()

    def extract_db_path(self):
        try:
            folder_path, file_name, extension = PathValidator.extract_path(self.path_params)
            self.db_path = PathValidator.get_full_path(folder_path, file_name, extension)
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.db_path()

    def connect(self):
        if self.connection:
            Messages.Error.connection_already_established(self.db_path)
            return

        try:
            PathValidator.for_read(self.path_params.get('folder_path', ''),
                                   self.path_params.get('file_name', ''),
                                   self.path_params.get('extension', ''),
                                   ['db'])
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.connection(self.db_path)
            return

        try:
            self.connection = sqlite3.connect(self.db_path)
            Messages.Complete.connection(self.db_path)
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.connection(self.db_path)
            return

    def close(self):
        if self.connection:
            try:
                self.connection.close()
                self.connection = None
                Messages.Complete.close_connection(self.db_path)
            except Exception as e:
                Messages.Error.try_action(e)
        else:
            Messages.Error.miss_connection(self.db_path)

    def create_db(self):
        self.close()
        self.connection = None

        if os.path.exists(self.db_path):
            Messages.Error.db_already_exist(self.db_path)
            Messages.Error.create_db(self.db_path)
        else:
            try:
                self.connection = sqlite3.connect(self.db_path)
                Messages.Complete.create_db(self.db_path)
                Messages.Complete.connection(self.db_path)
            except Exception as e:
                Messages.Error.try_action(e)
                Messages.Error.create_db(self.db_path)
                Messages.Error.connection(self.db_path)
                return

    def delete_db(self):
        self.close()
        self.connection = None

        if os.path.exists(self.db_path):
            try:
                os.remove(self.db_path)
                Messages.Complete.delete_db(self.db_path)
            except Exception as e:
                Messages.Error.try_action(e)
                Messages.Error.delete_db(self.db_path)
        else:
            Messages.Error.db_file_found(self.db_path)
            Messages.Error.delete_db(self.db_path)
