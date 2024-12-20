from ..connection.db_connection import DatabaseConnection
from ..table_config.table_config_loader import TableConfigLoader
from .db_manager import DatabaseManager


class DatabaseHandler:
    def __init__(self, config_path):
        self.db_config_path = config_path
        self.tables_config_path = config_path

        self.connection = None
        self.manager = None

    def setup(self):
        self.connection = DatabaseConnection(self.db_config_path)
        # self.connection.create_db()
        self.connection.connect()

        tables_config_loader = TableConfigLoader(self.tables_config_path)

        self.manager = DatabaseManager(self.connection, tables_config_loader)
        self.manager.init_tables()

    def run(self):
        self.manager.create_tables()

        # self.manager.tables['room_class'].insert_data(("507", 20))
        # self.manager.tables['room_class'].update_data(("507", 22), (3,))

        # self.manager.tables['room_class'].delete_data((6,))

        # data = self.manager.tables['room_class'].find_id(("507", ))
        # print("Data:", data)

        # data = self.manager.tables['room_class'].fetch_one((5,))
        # print("Data:", data)

        # data = self.manager.tables['room_class'].fetch_all()
        # print("Data:", data)

        # self.manager.tables['room'].insert_data(("Аудитория 1", 7))

        # data = self.manager.tables['room'].fetch_all()
        # print("Data:", data)

    def cleanup(self):
        # self.manager.drop_tables()
        # self.manager.delete_database()
        self.connection.close()
