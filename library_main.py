import json
import os
from main_classes import Library
from menu import menu
from utils import recreate_library

if __name__ == '__main__':
    print('Добро пожаловать в Библиотеку!')

    while True:
        """
        В этом блоке происходит создание новой библиотеки или загрузка существующей
        """
        try:
            start_option = int(input('\n1 - Создать новую библиотеку\n2 - Открыть существующую\n\n'))
            if start_option not in [1, 2]:
                print('Введите целое число от 1 до 2')
            elif start_option == 1:
                library_name = input('Введите название новой библиотеки: ').strip()
                library_name += '.json'
                new_library = Library()
                break
            elif start_option == 2:
                library_name = input('Библиотека должна находиться в одной папке с приложением\n'
                                     'Введите название библиотеки в формате `xxx.json`: ')
                library_path = os.path.abspath(library_name)
                if os.path.exists(library_path):
                    print('Библиотека загружена')
                    with open(library_name, 'r', encoding='utf-8') as library_storage:
                        library_data = json.load(library_storage)
                        new_library = recreate_library(library_data)
                    break
                else:
                    print(
                        'Библиотека не найдена. Проверьте название и убедитесь, что библиотека находится в одной папке с приложением')

        except (TypeError, ValueError):
            print('Для использования библиотеки, введите номер команды из списка')

    while True:
        """
        В этом блоке вызывается основное меню
        """
        result = menu(new_library)
        if result == 0:
            break
        if result and result != 0:
            with open(library_name, 'w', encoding='utf-8') as library_storage:
                json.dump(result, library_storage, indent=4, ensure_ascii=False)
