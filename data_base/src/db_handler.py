from ..connection.db_connection import DatabaseConnection
from ..table_config.table_config_loader import TableConfigLoader
from .db_manager import DatabaseManager


class DatabaseHandler:
    def __init__(self, db_path, config_folder_path):
        self.db_path = db_path
        self.config_folder_path = config_folder_path
        self.connection = None
        self.manager = None

    def setup(self):
        self.connection = DatabaseConnection(self.db_path)
        # self.connection.create_db()
        self.connection.connect()

        config_loader = TableConfigLoader(self.config_folder_path)

        self.manager = DatabaseManager(self.connection, config_loader)
        self.manager.init_tables()

    def run(self):
        self.manager.create_tables()

        self.manager.tables['room_class'].insert_data((1, 50))
        self.manager.tables['room_class'].update_data((2, 60), (1,))

        data = self.manager.tables['room_class'].fetch_all()
        print("Data from room_class:", data)

        self.manager.tables['room_class'].delete_data((1,))

        data_after_deletion = self.manager.tables['room_class'].fetch_all()
        print("Data after deletion:", data_after_deletion)

    def cleanup(self):
        # self.manager.drop_tables()
        # self.manager.delete_database()
        self.connection.close()
