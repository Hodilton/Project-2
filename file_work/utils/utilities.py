import os

class Messages:
    class Complete:
        @staticmethod
        def data_read(data_path):
            print(f"Data '{data_path}' read successfully.")

        @staticmethod
        def data_write(data_path):
            print(f"Data '{data_path}' written successfully.")

    class Error:
        @staticmethod
        def data_read(data_path):
            print(f"Data '{data_path}' was not read.")

        @staticmethod
        def data_write(data_path):
            print(f"Data '{data_path}' was not written.")

        @staticmethod
        def try_action(exception):
            print(f"An error occurred: '{exception}'.")

        @staticmethod
        def file_format_not_supported(extension):
            print(f"File format '{extension}' is not supported.")

        @staticmethod
        def specified_dictionary(specified_keys):
            print(f"Required keys are not specified: {', '.join(specified_keys)}.")

        @staticmethod
        def file_not_found(file_path):
            print(f"File '{file_path}' not found.")

        @staticmethod
        def file_found(file_path):
            print(f"File '{file_path}' already exists.")

        @staticmethod
        def folder_not_found(folder_path):
            print(f"Folder '{folder_path}' not found.")

        @staticmethod
        def file_extension(file_path, valid_extensions):
            print(f"File '{file_path}' has an invalid extension."
                  f" Valid extension: {', '.join(valid_extensions)}.")

class Check:
    @staticmethod
    def dictionary_specified(dictionary, specified):
        for key in specified:
            if key not in dictionary:
                return False
        return True

    @staticmethod
    def file_file(file_path):
        return os.path.isfile(file_path)

    @staticmethod
    def file_directory(file_path):
        return os.path.isdir(file_path)

    @staticmethod
    def file_extension(extension, valid_extensions):
        return extension.lower() in valid_extensions