class Messages:
    class Complete:
        @staticmethod
        def connection(db_path):
            print(f"The connection to Database {db_path} was successful.")

        @staticmethod
        def close_connection(db_path):
            print(f"The connection to Database {db_path} was successful close.")

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
        def specified_dictionary(specified_keys):
            print(f"Required keys are not specified: {', '.join(specified_keys)}.")

        @staticmethod
        def file_extension(file_path, valid_extensions):
            print(f"File '{file_path}' has an invalid extension."
                  f"Valid extension: {', '.join(valid_extensions)}.")