-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: MySQL-8.2
-- Время создания: Дек 21 2024 г., 09:06
-- Версия сервера: 8.2.0
-- Версия PHP: 8.1.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `project`
--

-- --------------------------------------------------------

--
-- Структура таблицы `authors`
--

CREATE TABLE `authors` (
  `id` int NOT NULL,
  `LastName` varchar(255) NOT NULL,
  `MiddleName` varchar(255) DEFAULT NULL,
  `SecondName` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `authors`
--

INSERT INTO `authors` (`id`, `LastName`, `MiddleName`, `SecondName`) VALUES
(1, 'Пушкин', 'Александр', 'Сергеевич'),
(2, 'Толстой', 'Лев', 'Николаевич'),
(3, 'Достоевский', 'Фёдор', 'Михайлович'),
(4, 'Гоголь', 'Николай', 'Васильевич'),
(5, 'Тургенев', 'Иван', 'Сергеевич'),
(6, 'Булгаков', 'Михаил', 'Афанасьевич'),
(7, 'Чехов', 'Антон', 'Павлович'),
(8, 'Есенин', 'Сергей', 'Александрович'),
(9, 'Блок', 'Александр', 'Александрович'),
(10, 'Маяковский', 'Владимир', 'Владимирович');

-- --------------------------------------------------------

--
-- Структура таблицы `books`
--

CREATE TABLE `books` (
  `id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `id_genre` int NOT NULL,
  `id_author` int NOT NULL,
  `year_published` smallint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `books`
--

INSERT INTO `books` (`id`, `title`, `id_genre`, `id_author`, `year_published`) VALUES
(1, 'Евгений Онегин', 1, 1, 1833),
(2, 'Война и мир', 1, 2, 1869),
(3, 'Преступление и наказание', 1, 3, 1866),
(4, 'Мёртвые души', 1, 4, 1842),
(5, 'Отцы и дети', 1, 5, 1862),
(6, 'Мастер и Маргарита', 1, 6, 1940),
(7, 'Вишнёвый сад', 1, 7, 1904),
(8, 'Анна Каренина', 1, 2, 1877),
(9, 'Доктор Живаго', 1, 2, 1957),
(10, 'Двенадцать', 1, 8, 1918);

-- --------------------------------------------------------

--
-- Структура таблицы `book_statuses`
--

CREATE TABLE `book_statuses` (
  `id` int NOT NULL,
  `status_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `book_statuses`
--

INSERT INTO `book_statuses` (`id`, `status_name`) VALUES
(1, 'Выдана'),
(2, 'Возвращена'),
(3, 'Зарезервирована'),
(4, 'Утеряна');

-- --------------------------------------------------------

--
-- Структура таблицы `borrowed_books`
--

CREATE TABLE `borrowed_books` (
  `id` int NOT NULL,
  `date_from` date NOT NULL,
  `date_to` date DEFAULT NULL,
  `id_book_status` int NOT NULL,
  `id_book` int NOT NULL,
  `id_reader` int NOT NULL,
  `id_librarian` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `borrowed_books`
--

INSERT INTO `borrowed_books` (`id`, `date_from`, `date_to`, `id_book_status`, `id_book`, `id_reader`, `id_librarian`) VALUES
(1, '2024-01-01', '2024-01-15', 1, 1, 1, 1),
(2, '2024-01-02', '2024-01-16', 1, 2, 2, 2),
(3, '2024-01-03', '2024-01-17', 2, 3, 3, 3),
(4, '2024-01-04', '2024-01-18', 3, 4, 4, 4),
(5, '2024-01-05', '2024-01-19', 4, 5, 5, 5),
(6, '2024-05-06', '2024-07-07', 3, 6, 5, 3);

-- --------------------------------------------------------

--
-- Структура таблицы `departments`
--

CREATE TABLE `departments` (
  `id` int NOT NULL,
  `department_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `departments`
--

INSERT INTO `departments` (`id`, `department_name`) VALUES
(1, 'Обслуживание'),
(2, 'Читальный зал'),
(3, 'Абонемент'),
(4, 'Архив'),
(5, 'Информационный отдел');

-- --------------------------------------------------------

--
-- Структура таблицы `genres`
--

CREATE TABLE `genres` (
  `id` int NOT NULL,
  `genre_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `genres`
--

INSERT INTO `genres` (`id`, `genre_name`) VALUES
(6, 'Биография'),
(5, 'Детектив'),
(8, 'Детская литература'),
(7, 'История'),
(2, 'Научная литература'),
(9, 'Романтика'),
(10, 'Ужасы'),
(3, 'Фантастика'),
(4, 'Фэнтези'),
(1, 'Художественная литература');

-- --------------------------------------------------------

--
-- Структура таблицы `librarians`
--

CREATE TABLE `librarians` (
  `id` int NOT NULL,
  `LastName` varchar(255) NOT NULL,
  `MiddleName` varchar(255) DEFAULT NULL,
  `SecondName` varchar(255) DEFAULT NULL,
  `id_department` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `librarians`
--

INSERT INTO `librarians` (`id`, `LastName`, `MiddleName`, `SecondName`, `id_department`) VALUES
(1, 'Ковалёв', 'Евгений', 'Александрович', 1),
(2, 'Михайлова', 'Ольга', 'Викторовна', 2),
(3, 'Семенова', 'Ирина', 'Сергеевна', 3),
(4, 'Воронов', 'Андрей', 'Петрович', 4),
(5, 'Павлова', 'Татьяна', 'Николаевна', 5);

-- --------------------------------------------------------

--
-- Структура таблицы `readers`
--

CREATE TABLE `readers` (
  `id` int NOT NULL,
  `LastName` varchar(255) NOT NULL,
  `MiddleName` varchar(255) DEFAULT NULL,
  `SecondName` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `readers`
--

INSERT INTO `readers` (`id`, `LastName`, `MiddleName`, `SecondName`) VALUES
(1, 'Иванов', 'Иван', 'Иванович'),
(2, 'Петров', 'Петр', 'Сергеевич'),
(3, 'Сидоров', 'Алексей', 'Николаевич'),
(4, 'Кузнецов', 'Дмитрий', 'Викторович'),
(5, 'Смирнова', 'Мария', 'Александровна'),
(6, 'Попова', 'Елена', 'Сергеевна'),
(7, 'Васильев', 'Игорь', 'Павлович'),
(8, 'Козлова', 'Анна', 'Михайловна'),
(9, 'Зайцева', 'Ольга', 'Ивановна'),
(10, 'Морозов', 'Никита', 'Сергеевич');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_genre` (`id_genre`),
  ADD KEY `id_author` (`id_author`);

--
-- Индексы таблицы `book_statuses`
--
ALTER TABLE `book_statuses`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `borrowed_books`
--
ALTER TABLE `borrowed_books`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_book_status` (`id_book_status`),
  ADD KEY `id_book` (`id_book`),
  ADD KEY `id_reader` (`id_reader`),
  ADD KEY `id_librarian` (`id_librarian`);

--
-- Индексы таблицы `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `genres`
--
ALTER TABLE `genres`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `genre_name` (`genre_name`);

--
-- Индексы таблицы `librarians`
--
ALTER TABLE `librarians`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_department` (`id_department`);

--
-- Индексы таблицы `readers`
--
ALTER TABLE `readers`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `authors`
--
ALTER TABLE `authors`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблицы `books`
--
ALTER TABLE `books`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблицы `book_statuses`
--
ALTER TABLE `book_statuses`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `borrowed_books`
--
ALTER TABLE `borrowed_books`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `departments`
--
ALTER TABLE `departments`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `genres`
--
ALTER TABLE `genres`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблицы `librarians`
--
ALTER TABLE `librarians`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `readers`
--
ALTER TABLE `readers`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_ibfk_1` FOREIGN KEY (`id_genre`) REFERENCES `genres` (`id`),
  ADD CONSTRAINT `books_ibfk_2` FOREIGN KEY (`id_author`) REFERENCES `authors` (`id`);

--
-- Ограничения внешнего ключа таблицы `borrowed_books`
--
ALTER TABLE `borrowed_books`
  ADD CONSTRAINT `borrowed_books_ibfk_1` FOREIGN KEY (`id_book_status`) REFERENCES `book_statuses` (`id`),
  ADD CONSTRAINT `borrowed_books_ibfk_2` FOREIGN KEY (`id_book`) REFERENCES `books` (`id`),
  ADD CONSTRAINT `borrowed_books_ibfk_3` FOREIGN KEY (`id_reader`) REFERENCES `readers` (`id`),
  ADD CONSTRAINT `borrowed_books_ibfk_4` FOREIGN KEY (`id_librarian`) REFERENCES `librarians` (`id`);

--
-- Ограничения внешнего ключа таблицы `librarians`
--
ALTER TABLE `librarians`
  ADD CONSTRAINT `librarians_ibfk_1` FOREIGN KEY (`id_department`) REFERENCES `departments` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
