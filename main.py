from data_base.src.db_handler import DatabaseHandler
from app.app_main import Application

from app.displays.display_base import DisplayBase

def main():
    db_path = {
        'folder_path': './data',
        'file_name': 'database',
        'extension': 'db'
    }

    db_handler = DatabaseHandler(db_path, db_path["folder_path"])

    try:
        frames_config = {
            "Аудитории": {
                "room_class": {
                    "class": DisplayBase,
                    "name": "Аудитории",
                },
            },
            "Сотрудники": {
                "staff": {
                    "class": DisplayBase,
                    "name": "Сотрудники",
                },
            },
        }

        # db_handler.setup()
        app = Application(frames_config, db_handler.manager)
        app.run()
        # db_handler.run()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # db_handler.cleanup()
        pass

if __name__ == "__main__":
    main()
