class Messages:
    class Complete:
        @staticmethod
        def connection(db_path):
            print(f"The connection to Database '{db_path}' was successful.")

        @staticmethod
        def close_connection(db_path):
            print(f"The connection to Database '{db_path}' was successful close.")

        @staticmethod
        def create_db(db_path):
            print(f"The Database {db_path} has been created.")

        @staticmethod
        def delete_db(db_path):
            print(f"The Database {db_path} has been deleted.")

        @staticmethod
        def db_load_config():
            print(f"The Database Config was uploaded.")

        @staticmethod
        def table_load_config():
            print(f"The Tables Config was uploaded.")

        @staticmethod
        def table_load_queries(table_name):
            print(f"Queries for table '{table_name}' was uploaded.")

        @staticmethod
        def table_initialized(table_name):
            print(f"Initialized table '{table_name}' with queries.")

        @staticmethod
        def table_creating(table_name):
            print(f"Table '{table_name}' created successfully.")

        @staticmethod
        def table_droping(table_name):
            print(f"Table '{table_name}' dropped successfully.")

    class Error:
        @staticmethod
        def try_action(exception):
            print(f"An error occurred: '{exception}'.")

        @staticmethod
        def connection(db_path):
            print(f"The connection to Database {db_path} was not successful.")

        @staticmethod
        def miss_connection(db_path):
            print(f"There is no connection to the Database {db_path}.")

        @staticmethod
        def db_path():
            print("Invalid database path configuration.")

        @staticmethod
        def create_db(db_path):
            print(f"The Database {db_path} was not created.")

        @staticmethod
        def delete_db(db_path):
            print(f"The Database {db_path} was not deleted.")

        @staticmethod
        def db_already_exist(db_path):
            print(f"The Database {db_path} already exists.")

        @staticmethod
        def db_file_found(db_path):
            print(f"The Database {db_path} file was not found.")

        @staticmethod
        def db_load_config():
            raise Exception(f"The Database Config was not uploaded.")

        @staticmethod
        def table_load_config():
            raise Exception(f"The Tables Config was not uploaded.")

        @staticmethod
        def table_load_queries(table_name):
            raise Exception(f"Queries for table '{table_name}' was not uploaded.")

        @staticmethod
        def table_found(table_name):
            print(f"Table '{table_name}' not found in configuration.")

        @staticmethod
        def connection_already_established(db_path):
            print(f"The connection to the Database {db_path} has already been established.")

        @staticmethod
        def table_initialized(table_name):
            print(f"Failed to initialize tables: '{table_name}'.")

        @staticmethod
        def table_creating(table_name):
            print(f"Error creating table '{table_name}.")

        @staticmethod
        def table_droping(table_name):
            print(f"Error dropping table '{table_name}'.")

        @staticmethod
        def data_inserting(table_name):
            print(f"Error inserting data into table '{table_name}'.")

        @staticmethod
        def data_updating(table_name):
            print(f"Error updating data in table '{table_name}'.")

        @staticmethod
        def data_deleting(table_name):
            print(f"Error deleting data from table '{table_name}'.")

        @staticmethod
        def data_fetching(table_name):
            print(f"Error fetching data from table '{table_name}'.")