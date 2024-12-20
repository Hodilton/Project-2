from data_base.src.db_handler import DatabaseHandler
from app.app_main import Application

from app.displays.display_base import DisplayBase
from app.displays.display_room import DisplayRoom
from app.displays.display_room_class import DisplayRoomClass

def main():
    db_handler = DatabaseHandler(config_path="./data")

    try:
        frames_config = {
            "Аудитории": {
                "room_class": {
                    "class": DisplayRoomClass,
                    "name": "Кабинет - места",
                },

                "room": {
                    "class": DisplayRoom,
                    "name": "Аудитории",
                },
            },
        }

        db_handler.setup()
        # db_handler.run()

        app = Application(frames_config, db_handler.manager)
        app.run()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db_handler.cleanup()

if __name__ == "__main__":
    main()
