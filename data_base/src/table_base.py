from data_base.utils.utilities import Messages


class TableBase:
    def __init__(self, connection, table_name, queries):
        self.connection = connection
        self.table_name = table_name
        self.queries = queries

    def create_table(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(self.queries['create'])
                self.connection.commit()
            Messages.Complete.table_creating(self.table_name)
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.table_creating(self.table_name)

    def drop_table(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(self.queries['drop'])
                self.connection.commit()
            Messages.Complete.table_droping(self.table_name)
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.table_droping(self.table_name)

    def insert_data(self, data):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(self.queries['insert'], data)
                self.connection.commit()
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.data_inserting(self.table_name)

    def update_data(self, data, condition):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(self.queries['update'], (*data, *condition))
                self.connection.commit()
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.data_updating(self.table_name)

    def delete_data(self, condition):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(self.queries['delete'], condition)
                self.connection.commit()
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.data_deleting(self.table_name)

    def find_id(self, condition):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(self.queries['find_id'], condition)
                result =  cursor.fetchone()

            if result:
                return result[0]
            else:
                Messages.Error.data_fetching(self.table_name)
                return None
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.data_fetching(self.table_name)
            return None

    def fetch_one(self, condition):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(self.queries['fetch_one'], condition)
                return cursor.fetchone()
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.data_fetching(self.table_name)
            return None

    def fetch_select(self, condition):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(self.queries['fetch_select'], condition)
                return cursor.fetchall()
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.data_fetching(self.table_name)
            return None

    def fetch_all(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(self.queries['fetch_all'])
                return cursor.fetchall()
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.data_fetching(self.table_name)
