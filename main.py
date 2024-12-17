from data_base.src.db_handler import DatabaseHandler


def main():
    db_path = {
        'folder_path': './data',
        'file_name': 'database',
        'extension': 'db'
    }

    db_handler = DatabaseHandler(db_path, db_path["folder_path"])

    try:
        db_handler.setup()
        # db_handler.run()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db_handler.cleanup()

if __name__ == "__main__":
    main()
