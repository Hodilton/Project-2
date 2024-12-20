from ..connection.db_connection import DatabaseConnection
from ..table_config.table_config_loader import TableConfigLoader
from .db_manager import DatabaseManager

'''
    self.manager.tables['genres'].insert_data(("Ужасы", ))
    self.manager.tables['genres'].update_data(("Ужасы", ), (1,))
    self.manager.tables['genres'].delete_data((1,))
    data = self.manager.tables['genres'].find_id(("Ужасы", )) 
    data = self.manager.tables['genres'].fetch_one((1,))
    data = self.manager.tables['genres'].fetch_all()
'''

class DatabaseHandler:
    def __init__(self, config_path):
        self.db_config_path = config_path
        self.tables_config_path = config_path

        self.connection = None
        self.manager = None

    def setup(self):
        self.connection = DatabaseConnection(self.db_config_path)
        # self.connection.create_db()
        self.connection.connect()

        tables_config_loader = TableConfigLoader(self.tables_config_path)

        self.manager = DatabaseManager(self.connection, tables_config_loader)
        self.manager.init_tables()

    def seed(self):
        # self.manager.drop_tables()
        # self.manager.create_tables()

        # self.manager.tables['genres'].insert_data(("Художественная литература",))
        # self.manager.tables['genres'].insert_data(("Научная литература",))
        # self.manager.tables['genres'].insert_data(("Фантастика",))
        # self.manager.tables['genres'].insert_data(("Фэнтези",))
        # self.manager.tables['genres'].insert_data(("Детектив",))
        # self.manager.tables['genres'].insert_data(("Биография",))
        # self.manager.tables['genres'].insert_data(("История",))
        # self.manager.tables['genres'].insert_data(("Детская литература",))
        # self.manager.tables['genres'].insert_data(("Романтика",))
        # self.manager.tables['genres'].insert_data(("Ужасы",))
        #
        # self.manager.tables['authors'].insert_data(("Пушкин", "Александр", "Сергеевич"))
        # self.manager.tables['authors'].insert_data(("Толстой", "Лев", "Николаевич"))
        # self.manager.tables['authors'].insert_data(("Достоевский", "Фёдор", "Михайлович"))
        # self.manager.tables['authors'].insert_data(("Гоголь", "Николай", "Васильевич"))
        # self.manager.tables['authors'].insert_data(("Тургенев", "Иван", "Сергеевич"))
        # self.manager.tables['authors'].insert_data(("Булгаков", "Михаил", "Афанасьевич"))
        # self.manager.tables['authors'].insert_data(("Чехов", "Антон", "Павлович"))
        # self.manager.tables['authors'].insert_data(("Есенин", "Сергей", "Александрович"))
        # self.manager.tables['authors'].insert_data(("Блок", "Александр", "Александрович"))
        # self.manager.tables['authors'].insert_data(("Маяковский", "Владимир", "Владимирович"))

        # self.manager.tables['book_statuses'].insert_data(("Выдана",))
        # self.manager.tables['book_statuses'].insert_data(("Возвращена",))
        # self.manager.tables['book_statuses'].insert_data(("Зарезервирована",))
        # self.manager.tables['book_statuses'].insert_data(("Утеряна",))

        # self.manager.tables['books'].insert_data(("Евгений Онегин", 1, 1, 1833))
        # self.manager.tables['books'].insert_data(("Война и мир", 1, 2, 1869))
        # self.manager.tables['books'].insert_data(("Преступление и наказание", 1, 3, 1866))
        # self.manager.tables['books'].insert_data(("Мёртвые души", 1, 4, 1842))
        # self.manager.tables['books'].insert_data(("Отцы и дети", 1, 5, 1862))
        # self.manager.tables['books'].insert_data(("Мастер и Маргарита", 1, 6, 1940))
        # self.manager.tables['books'].insert_data(("Вишнёвый сад", 1, 7, 1904))
        # self.manager.tables['books'].insert_data(("Анна Каренина", 1, 2, 1877))
        # self.manager.tables['books'].insert_data(("Доктор Живаго", 1, 2, 1957))
        # self.manager.tables['books'].insert_data(("Двенадцать", 1, 8, 1918))

        # self.manager.tables['departments'].insert_data(("Обслуживание",))
        # self.manager.tables['departments'].insert_data(("Читальный зал",))
        # self.manager.tables['departments'].insert_data(("Абонемент",))
        # self.manager.tables['departments'].insert_data(("Архив",))
        # self.manager.tables['departments'].insert_data(("Информационный отдел",))

        # self.manager.tables['librarians'].insert_data(("Ковалёв", "Евгений", "Александрович", 1))
        # self.manager.tables['librarians'].insert_data(("Михайлова", "Ольга", "Викторовна", 2))
        # self.manager.tables['librarians'].insert_data(("Семенова", "Ирина", "Сергеевна", 3))
        # self.manager.tables['librarians'].insert_data(("Воронов", "Андрей", "Петрович", 4))
        # self.manager.tables['librarians'].insert_data(("Павлова", "Татьяна", "Николаевна", 5))

        self.manager.tables['readers'].insert_data(("Иванов", "Иван", "Иванович"))
        self.manager.tables['readers'].insert_data(("Петров", "Петр", "Сергеевич"))
        self.manager.tables['readers'].insert_data(("Сидоров", "Алексей", "Николаевич"))
        self.manager.tables['readers'].insert_data(("Кузнецов", "Дмитрий", "Викторович"))
        self.manager.tables['readers'].insert_data(("Смирнова", "Мария", "Александровна"))
        self.manager.tables['readers'].insert_data(("Попова", "Елена", "Сергеевна"))
        self.manager.tables['readers'].insert_data(("Васильев", "Игорь", "Павлович"))
        self.manager.tables['readers'].insert_data(("Козлова", "Анна", "Михайловна"))
        self.manager.tables['readers'].insert_data(("Зайцева", "Ольга", "Ивановна"))
        self.manager.tables['readers'].insert_data(("Морозов", "Никита", "Сергеевич"))

        self.manager.tables['borrowed_books'].insert_data(("2024-01-01", "2024-01-15", 1, 1, 1, 1))
        self.manager.tables['borrowed_books'].insert_data(("2024-01-02", "2024-01-16", 1, 2, 2, 2))
        self.manager.tables['borrowed_books'].insert_data(("2024-01-03", "2024-01-17", 2, 3, 3, 3))
        self.manager.tables['borrowed_books'].insert_data(("2024-01-04", "2024-01-18", 3, 4, 4, 4))
        self.manager.tables['borrowed_books'].insert_data(("2024-01-05", "2024-01-19", 4, 5, 5, 5))

        pass

    def cleanup(self):
        # self.manager.drop_tables()
        # self.manager.delete_database()
        self.connection.close()
