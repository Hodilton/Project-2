from .table_base import TableBase
from ..utils.utilities import Messages


class DatabaseManager:
    def __init__(self, connection, config_loader):
        self.db_connection = connection
        self.config_loader = config_loader
        self.tables = {}

    def init_tables(self):
        for table_name, table_info in self.config_loader.tables_config.items():
            try:
                queries = self.config_loader.get_table_queries(table_name)
                self.tables[table_name] = TableBase(
                    connection=self.db_connection.connection,
                    table_name=table_name,
                    queries=queries
                )

                Messages.Complete.table_initialized(table_name)
            except Exception as e:
                Messages.Error.try_action(e)
                Messages.Error.table_initialized(table_name)

    def create_tables(self):
        for table_name, table_instance in self.tables.items():
            try:
                table_instance.create_table()
            except Exception as e:
                Messages.Error.try_action(e)

    def drop_tables(self):
        for table_name, table_instance in self.tables.items():
            try:
                table_instance.drop_table()
                Messages.Complete.table_droping(table_name)
            except Exception as e:
                Messages.Error.try_action(e)

    def delete_database(self):
        try:
            self.db_connection.delete_db()
        except Exception as e:
            Messages.Error.try_action(e)

    def insert_data(self, table_name, data):
        if table_name not in self.tables:
            Messages.Error.table_found(table_name)
            return
        try:
            self.tables[table_name].insert_data(data)
        except Exception as e:
            Messages.Error.try_action(e)

    def update_data(self, table_name, data, condition):
        if table_name not in self.tables:
            Messages.Error.table_found(table_name)
            return
        try:
            self.tables[table_name].update_data(data, condition)
        except Exception as e:
            Messages.Error.try_action(e)

    def delete_data(self, table_name, condition):
        if table_name not in self.tables:
            Messages.Error.table_found(table_name)
            return
        try:
            self.tables[table_name].delete_data(condition)
        except Exception as e:
            Messages.Error.try_action(e)

    def fetch_all(self, table_name):
        if table_name not in self.tables:
            Messages.Error.table_found(table_name)
            return []
        try:
            data = self.tables[table_name].fetch_all()
            return data
        except Exception as e:
            Messages.Error.try_action(e)
            return []
