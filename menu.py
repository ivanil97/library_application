from typing import Optional

from main_classes import Library
from utils import year_check


def menu(user_library: Library) -> Optional[int]:
    """
    Функция, представляющая интерфейс для управления библиотекой
    :param user_library: Библиотека (объект класса Library)
    :return: Optional[int]
    """
    try:
        choice = int(input(
            '\n1 - Добавить книгу\n2 - Удалить книгу\n3 - Поиск книги\n4 - Отобразить все книги\n'
            '5 - Изменить статус книги\n0 - Завершить работу с библиотекой\n\n'))

        if choice == 0:
            """
            Завершение работы с библиотекой
            """
            return 0

        elif choice == 1:
            """
            В этом блоке реализован функционал добавления книги
            """
            while True:
                try:
                    title_input = input('Введите название книги: ')
                    author_input = input('Введите автора книги: ')
                    year_input = input('Введите год издания: ')

                    if not title_input or not author_input or not year_input:
                        raise ValueError('Для добавления книги укажите все необходимые параметры\n')
                    if not year_check(year_input):
                        raise ValueError('Год должен быть в формате YYYY\n')

                    title, author, year = title_input, author_input, year_input
                    result = user_library.add_book(title, author, year)
                    print(result)
                    return user_library.library_dict
                except ValueError as exc:
                    print(exc)

        elif choice == 2:
            """
            В этом блоке реализован функционал удаления книги
            """
            while True:
                try:
                    user_input = int(input('Введите ID книги, который хотите удалить: '))
                    result = user_library.remove_book(user_input)
                    print(result['message'])
                    if result['status']:
                        return user_library.library_dict
                    else:
                        return None
                except (TypeError, ValueError):
                    print('ID книги должен быть целым числом\n')

        elif choice == 3:
            """
            В этом блоке реализован функционал поиска по названию, автору, году выпуска
            """
            while True:
                try:
                    user_option = int(input('Выберите критерий поиска: 1 - Название, 2 - Автор, 3 - Год издания\n'))
                    if user_option not in [1, 2, 3]:
                        print('Введите целое число от 1 до 3')
                    else:
                        break
                except (TypeError, ValueError):
                    print('Введите целое число от 1 до 3')
            user_input = input('Введите сообщение для поиска: ')
            result = user_library.search_book(user_option, user_input)
            print(result)

        elif choice == 4:
            """
            В этом блоке реализован для отображения списка всех книг в библиотеке
            """
            result = user_library.show_all_books()
            if result:
                print('Список книг в библиотеке:\n' + '\n'.join(result))
            else:
                print('Библиотека пуста\n')

        elif choice == 5:
            """
            В этом блоке реализован функционал изменения статуса книги (в наличии/выдана)
            """
            while True:
                try:
                    book_id = int(input('Введите ID книги, статус которой вы хотите поменять: '))
                    break
                except (TypeError, ValueError):
                    print('ID книги должен быть целым числом\n')

            while True:
                try:
                    user_option = int(input('Выберите новый статус: 1 - В наличии, 2 - Выдана\n'))
                    if user_option not in [1, 2]:
                        print('Введите целое число от 1 до 2')
                    else:
                        break
                except (TypeError, ValueError):
                    print('Введите целое число от 1 до 2')

            result = user_library.change_status(book_id, user_option)
            print(result['message'])
            if result['status']:
                return user_library.library_dict
            else:
                return None

    except (TypeError, ValueError):
        print('Для использования библиотеки, введите номер команды из списка')
