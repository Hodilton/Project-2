from data_base.src.db_handler import DatabaseHandler
from app.app_main import Application
from app.frames.frames_config import frames_config

def main():
    db_handler = DatabaseHandler(config_path="./data")

    try:
        db_handler.setup()
        # db_handler.run()
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        app = Application(frames_config, db_handler.manager)
        app.run()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db_handler.cleanup()

if __name__ == "__main__":
    main()
