from file_work.src.file_processor import FileProcessor
from ..utils.utilities import Messages


class TableConfigLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.tables_config = {}

        self.load_config()

    def load_config(self):
        config_path = {
            'folder_path': self.folder_path,
            'file_name': 'tables_config',
            'extension': 'json'
        }

        try:
            self.tables_config = FileProcessor.read_file(config_path)
            Messages.Complete.table_load_config()
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.table_load_config()

    def get_table_queries(self, table_name):
        queries_path = {
            'folder_path': f"{self.folder_path}/queries",
            'file_name': table_name,
            'extension': 'json'
        }

        try:
            data = FileProcessor.read_file(queries_path)
            Messages.Complete.table_load_queries(table_name)
            return data
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.table_load_queries(table_name)
