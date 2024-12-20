import os
import mysql.connector
from mysql.connector import errorcode

from .db_config_loader import DBConfigLoader
from file_work.path_validator.path_validator import PathValidator
from ..utils.utilities import Messages

class DatabaseConnection:
    def __init__(self, db_config_path):
        self.db_config_path = db_config_path

        self.db_config = None
        self.connection = None

        self.load_db_config()

    def load_db_config(self):
        db_config_loader = DBConfigLoader(self.db_config_path)
        db_config_loader.load_config()
        self.db_config = db_config_loader.db_config

    def connect(self):
        if self.connection:
            Messages.Error.connection_already_established(self.db_config.get('database'))
            return

        try:
            self.connection = mysql.connector.connect(
                host=self.db_config.get('host'),
                user=self.db_config.get('user'),
                password=self.db_config.get('password'),
                database=self.db_config.get('database')
            )

            Messages.Complete.connection(self.db_config.get('database'))
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                Messages.Error.try_action("Access denied: Check your username or password.")
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                Messages.Error.try_action("Database does not exist.")
            else:
                Messages.Error.try_action(e)
            Messages.Error.connection(self.db_config.get('database'))
            return

    def close(self):
        if self.connection:
            try:
                self.connection.close()
                self.connection = None
                Messages.Complete.close_connection(self.db_config.get('database'))
            except Exception as e:
                Messages.Error.try_action(e)
        else:
            Messages.Error.miss_connection(self.db_config.get('database'))

    def create_db(self):
        try:
            self.close()
            self.connection = None

            with mysql.connector.connect(
                    host=self.db_config.get('host'),
                    user=self.db_config.get('user'),
                    password=self.db_config.get('password')
            ) as conn:
                cursor = conn.cursor()
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_config.get('database')}")
                Messages.Complete.create_db(self.db_config.get('database'))
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.create_db(self.db_config.get('database'))

    def delete_db(self):
        try:
            self.close()
            self.connection = None

            with mysql.connector.connect(
                    host=self.db_config.get('host'),
                    user=self.db_config.get('user'),
                    password=self.db_config.get('password')
            ) as conn:
                cursor = conn.cursor()
                cursor.execute(f"DROP DATABASE IF EXISTS {self.db_config.get('database')}")
                Messages.Complete.delete_db(self.db_config.get('database'))
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.delete_db(self.db_config.get('database'))
