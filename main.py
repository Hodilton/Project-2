import json

from file_work.src.file_processor import FileProcessor
from data_base.connection.db_connection import DatabaseConnection

def main():
    json_data = {'name': 'Alice',
                 'age': 30,
                 'city': 'New York'}

    path_params = {
        'folder_path': './data',
        'file_name': 'data',
        'extension': 'json'
    }

    # FileProcessor.write_file(path_params, json_data, overwrite=True)

    data = FileProcessor.read_file(path_params)
    print("Read data:", data)

    db_path_params = {
        'folder_path': './data',
        'file_name': 'database',
        'extension': 'db'
    }

    db_connection = DatabaseConnection(db_path_params)
    db_connection.close()

    # path_params = {
    #     'folder_path': './data',
    #     'file_name': 'binary_file',
    #     'extension': 'bin'
    # }
    #
    # json_string = json.dumps(json_data)
    # FileProcessor.write_file(path_params, json_string, overwrite=True)
    #
    # data = FileProcessor.read_file(path_params)
    # json_data_new = json.loads(data)
    # print("Read binary data:", json_data_new)

if __name__ == '__main__':
    main()
