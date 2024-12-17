from data_base.utils.utilities import Messages


class TableBase:
    def __init__(self, connection, table_name, queries):
        self.connection = connection
        self.table_name = table_name
        self.queries = queries

    def create_table(self):
        try:
            self.connection.execute(self.queries['create'])
            Messages.Complete.table_creating(self.table_name)
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.table_creating(self.table_name)

    def drop_table(self):
        try:
            self.connection.execute(self.queries['drop'])
            Messages.Complete.table_droping(self.table_name)
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.table_droping(self.table_name)

    def insert_data(self, data):
        try:
            self.connection.execute(self.queries['insert'], data)
            self.connection.commit()
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.data_inserting(self.table_name)

    def update_data(self, data, condition):
        try:
            self.connection.execute(self.queries['update'], (*data, *condition))
            self.connection.commit()
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.data_updating(self.table_name)

    def delete_data(self, condition):
        try:
            self.connection.execute(self.queries['delete'], condition)
            self.connection.commit()
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.data_deleting(self.table_name)

    def fetch_all(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(self.queries['select_all'])
            return cursor.fetchall()
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.data_fetching(self.table_name)
