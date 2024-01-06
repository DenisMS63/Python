from logger import *
from copy_data import *

def interface1():
    with open("phonebook.txt", "a", encoding="UTF-8"):
        pass

    command = "-1"
    while command != "5":
        print("\nВозможные варианты поиска:\n"
            "1. Добавить контакт\n"
            "2. Вывести на экран\n"
            "3. Поиск контакта\n"
            "4. Копирование данных\n"
            "5. Завершить работу")
        command = input("\nВведите пункт меню: ")
        print()

        while command not in ("1", "2", "3", "4", "5"):
            print("\nНекорректный ввод данных")
            command = input("\nВведите пункт меню: ")

        match command:
            case "1":
                add_contact(create_contact())
            case "2":
                show_info()
            case "3":
                search_contact()
            case "4":
                copy_data()
            case "5":
                print("Поиск успешно завершен!")

