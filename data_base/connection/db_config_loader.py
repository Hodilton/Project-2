from file_work.src.file_processor import FileProcessor
from ..utils.utilities import Messages

class DBConfigLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.db_config = {}

    def load_config(self):
        config_path = {
            'folder_path': self.folder_path,
            'file_name': 'db_config',
            'extension': 'json'
        }

        try:
            self.db_config = FileProcessor.read_file(config_path)
            Messages.Complete.db_load_config()
        except Exception as e:
            Messages.Error.try_action(e)
            Messages.Error.db_load_config()
