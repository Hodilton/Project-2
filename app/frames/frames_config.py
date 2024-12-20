from app.displays.display_base import DisplayBase
from app.displays.display_genres import DisplayGenres
from app.displays.book_statuses import DisplayBookStatuses
from app.displays.display_books import DisplayBooks
from app.displays.display_authors import DisplayAuthors


frames_config = {

    "Книги": {

        "books": {
            "class": DisplayBooks,
            "name": "Книги",
        },

        "genres": {
            "class": DisplayGenres,
            "name": "Жанры",
        },

        "book_statuses": {
            "class": DisplayBookStatuses,
            "name": "Статус книги",
        },

        "authors": {
            "class": DisplayAuthors,
            "name": "Авторы",
        },
    },
}