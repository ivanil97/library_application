from datetime import datetime
from typing import Dict

from main_classes import Library, Book


def recreate_library(library_data: Dict) -> Library:
    """
    Функция для загрузки библиотеки из словаря с данными
    :param library_data: Dict
    :return: Библиотека (объект класса Library)
    """
    new_library = Library()
    for book_id, i_book in library_data.items():
        new_library.add_book(
            title=i_book['title'],
            author=i_book['author'],
            year=i_book['year'],
            book_id=int(book_id)
        )

    last_book_id = int(list(library_data.keys())[-1])
    Book.last_id = last_book_id

    return new_library

def year_check(year_input: str) -> bool:
    """
    Функция для валидации введенного года издания книги
    :param year_input: Год выпуска
    :return: bool
    """
    current_year = datetime.now().year
    if len(year_input) == 4 and int(year_input) <= current_year:
        return True
    else:
        return False
