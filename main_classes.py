from typing import Optional, Dict, List


class Library:
    """
    Класс, представляющий библиотеку.
    Хранит в себе книги (объекты класса Book) и функционал по добавлению, удалению, поиску, изменению статуса книг
    """

    def __init__(self) -> None:
        """
        Метод, инициализирующий объект класса Library
        Атрибуты:
            book_shelf (dict): словарь, где ключ id книги, а значение объект класса Book.
            library_dict (Optional[Dict]): атрибут, в котором хранится детализированная информация о книгах
        """
        self.book_shelf = dict()
        self.library_dict = None

    def save_library(self) -> None:
        """
        Сохраняет детализированную информацию о книгах в виде словаря.
        Содержит id книги, название, автора, год издания, статус
        :return: None
        """
        new_library_dict = {
            book_id: {
                'title': i_book.title,
                'author': i_book.author,
                'year': i_book.year,
                'status': i_book.status,
            }
            for book_id, i_book in self.book_shelf.items()
        }
        self.library_dict = new_library_dict

    def add_book(self, title: str, author: str, year: str, book_id: Optional[int] = None) -> str:
        """
        Метод, добавляющий книгу в библиотеку
        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания
        :param book_id: id книги (генерируется автоматически, если не предоставлен)
        :return: Сообщение об успешном добавлении книги
        """

        if book_id:
            new_book = Book(title, author, year, book_id)
        else:
            new_book = Book(title, author, year)

        self.book_shelf[new_book.id] = new_book
        self.save_library()
        return 'Книга успешно добавлена'

    def remove_book(self, book_id: int) -> Dict:
        """
        Метод, удаляющий книгу из библиотеки
        :param book_id: id книги
        :return: Словарь с результатом операции (status, message)
        """
        if book_id in self.book_shelf.keys():
            self.book_shelf.pop(book_id)
            self.save_library()
            return {'status': 'success', 'message': 'Книга удалена'}
        else:
            return {'status': None, 'message': 'Книга с данным ID отсутствует'}

    def search_book(self, option: int, keyword: str) -> str:
        """
        Метод для поиска книг в библиотеке по названию, автору, году издания
        :param option: флаг для выбора критерия поиска (1- название, 2- автор, 3- год издания)
        :param keyword: Строка для поиска
        :return: Книги, найденные по запросу пользователя или сообщение об отсутствии совпадений
        :raises ValueError: Если опция не является целым числом от 1 до 3
        """
        if option == 1:
            key_search = 'title'
        elif option == 2:
            key_search = 'author'
        elif option == 3:
            key_search = 'year'
        else:
            raise ValueError('Введите целое число от 1 до 3')

        if not self.book_shelf:
            return 'Библиотека пуста'
        else:
            search_result = [str(i_book) for i_book in self.book_shelf.values() if
                             getattr(i_book, key_search).lower() == keyword.lower()]
            if search_result:
                return 'По вашему запросу найдено:\n' + '\n'.join(search_result)
            else:
                return 'По данному запросу книг не найдено'

    def show_all_books(self) -> Optional[List[str]]:
        """
        Метод для отображения всех книг в библиотеке
        :return: Список всех книг или None
        """
        if self.book_shelf:
            return list(map(str, self.book_shelf.values()))
        else:
            return None

    def change_status(self, book_id: int, new_status: int):
        """
        Метод для смены статуса книги в библиотеке
        :param book_id: id книги
        :param new_status: флаг для смены статуса книги (1 - в наличии, 2 - выдана)
        :return:  Словарь с результатом операции (status, message)
        """
        if book_id in self.book_shelf.keys():
            if new_status == 1:
                self.book_shelf[book_id].status = 'в наличии'
            elif new_status == 2:
                self.book_shelf[book_id].status = 'выдана'
            self.save_library()
            return {'status': 'success', 'message': 'Статус обновлен'}
        else:
            return {'status': None, 'message': 'Книга с данным ID отсутствует'}


class Book:
    """
    Класс, представляющий книгу
    Атрибуты:
        last_id (int): номер последнего созданного объекта Book
    """

    last_id: int = 0

    def __init__(self, title, author, year, book_id=None):
        """
        Метод, инициализирующий объект класса Book
        Аргументы:
            title (str): Название книги
            author (str): Автор книги
            year (str): год издания
            id (int): id книги (генерируется автоматически, если не предоставлен)
        """
        Book.last_id += 1
        if book_id:
            self.id = book_id
        else:
            self.id = Book.last_id
        self.title = title
        self.author = author
        self.year = year
        self.status = 'в наличии'

    def __str__(self):
        """
        Метод, возвращающий строковое представление книги
        :return: Строковое представление книги со всеми атрибутами
        """
        return f'id: {self.id} - "{self.title}", {self.author}, {self.year}г., {self.status}'
