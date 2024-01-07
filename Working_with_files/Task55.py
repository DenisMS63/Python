# Создать телефонный справочник с возможностью импорта 
# и экспорта данных в формате .txt . Фамилия, имя, отчество, 
# номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом формате
# 3. Пользователь может ввести одну из характеристик для поиска
# определенной записи (например имя или фаилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# 1. Создать телефонный справочник:                      +
#     - открыть файл для добавления данных (режим: а)   +
# 2. Добавить контакт:                                   +
#     - запросить информацию у пользователя             +
#     - подготовить данные под нужный формат            +
#     - открыть файл для добавления данных (режим: а)   +
#     - добавить данные в файл                          +
# 3. Вывести данные на экран:                            +
#     - открыть файл в режиме чтения (режим: r)         +
#     - вывести информацию на экран                     +
# 4. Поиск данных:                                       +
#     - запросить вариант поиска                        +
#     - запросить данные поиска                         +
#     - открыть файл в режиме чтения (режим: r)         +
#     - сохранить данные в переменную                   +
#     - осуществить поиск                               +
#     - вывести информацию на экран                     +
# 5. Реализовать пользовательский интерфейс (UI):        +
#     - вывести варианты меню                           +
#     - получения запроса пользователя                  +
#     - реализация запроса пользователя                 +
#     - реализовать выход из программы                  +
# 6. Копирование данных из одного файла в другой:                    +
#     - добавить в UI пункт копирование данных в новый документ     +
#     - реализовать копирования данных по выведенному списку        +
#     - добавить метод pick_copy()                                  +
#     - добавить метод all_copy()                                   +
#     - добавить метод finish_copy()                                +    

# def input_name():
#     return input("Введите имя: ")
# def input_surname():
#     return input("Введите фамилию: ")
# def input_patronymic():
#     return input("Введите отчество: ")
# def input_phone():
#     return input("Введите номер телефона: ")
# def input_address():
#     return input("Введите адрес: ")

# def create_contact():
#     surname = input_surname()
#     name = input_name()
#     patronymic = input_patronymic()
#     phone = input_phone()
#     address = input_address()
#     return f"{surname} {name} {patronymic}\n{phone}\n{address}\n\n"

# def add_contact(contact):
#     # contact = create_contact()
#     with open("phonebook.txt", "a", encoding="UTF-8") as file:
#         file.write(contact)

# def show_info():
#     with open("phonebook.txt", "r", encoding="UTF-8") as file:
#         list_contact = file.read().rstrip().split("\n\n")
#         for contact in enumerate(list_contact, 1):
#             print(*contact)                                     # распаковка для вывода в удобном виде с нумирацией
#             print()

#         # print(file.read())
#         # print(*enumerate(list_contact, 1))                      # каждый контакт нумеруется, начиная с 1

# def search_contact():
#     how_search = input(
#         "Выбирите вариант поиска: \n"
#         "1. По фамилии\n"
#         "2. По имени\n"
#         "3. По отчеству\n"
#         "4. По номеру\n"
#         "5. По адресу\n"
#         "Ввод: "
#     )
    
#     search = input("Введите данные для поиска: ")

#     while how_search not in ("1", "2", "3", "4", "5"):
#             print("\nНекорректный ввод данных")
#             how_search = input("\nВведите вариант поиска: ")

#     index_how_search = int(how_search) - 1
#     print()

#     with open("phonebook.txt", "r", encoding="UTF-8") as file:
#         list_contact = file.read().rstrip().split("\n\n")       # ф-я rstrip() для того чтобы не получался пустой список и не было ошибки: list out of range

#     for str_contact in list_contact:
#         new_list_contact = str_contact.replace("\n", " ").split()
#         # print(new_list_contact)
#         if search in new_list_contact[index_how_search]:
#             print(str_contact)
#             # print(new_list_contact)
#             print()

# def interface():
#     with open("phonebook.txt", "a", encoding="UTF-8"):
#         pass

#     command = "-1"
#     while command != "4":
#         print("\nВозможные варианты поиска:\n"
#             "1. Добавить контакт\n"
#             "2. Вывести на экран\n"
#             "3. Поиск контакта\n"
#             "4. Закончить поиск")
#         command = input("\nВведите пункт меню: ")
#         print()

#         while command not in ("1", "2", "3", "4"):
#             print("\nНекорректный ввод данных")
#             command = input("\nВведите пункт меню: ")

#         match command:
#             case "1":
#                 add_contact(create_contact())
#             case "2":
#                 show_info()
#             case "3":
#                 search_contact()
#             case "4":
#                 print("Поиск успешно завершен!")



# interface()
    
