from date_create import *

def show_info():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        list_contact = file.read().rstrip().split("\n\n")
        for contact in enumerate(list_contact, 1):
            print(*contact)                                     # распаковка для вывода в удобном виде с нумирацией
            print()

        # print(file.read())
        # print(*enumerate(list_contact, 1))                      # каждый контакт нумеруется, начиная с 1

def search_contact():
    how_search = input(
        "Выбирите вариант поиска: \n"
        "1. По фамилии\n"
        "2. По имени\n"
        "3. По отчеству\n"
        "4. По номеру\n"
        "5. По адресу\n"
        "Ввод: "
    )
    
    search = input("Введите данные для поиска: ")

    while how_search not in ("1", "2", "3", "4", "5"):
            print("\nНекорректный ввод данных")
            how_search = input("\nВведите вариант поиска: ")

    index_how_search = int(how_search) - 1
    print()

    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        list_contact = file.read().rstrip().split("\n\n")       # ф-я rstrip() для того чтобы не получался пустой список и не было ошибки: list out of range

    for str_contact in list_contact:
        new_list_contact = str_contact.replace("\n", " ").split()
        # print(new_list_contact)
        if search in new_list_contact[index_how_search]:
            print(str_contact)
            # print(new_list_contact)
            print()


def add_contact(contact):
    # contact = create_contact()
    with open("phonebook.txt", "a", encoding="UTF-8") as file:
        file.write(contact)


def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f"{surname} {name} {patronymic}\n{phone}\n{address}\n\n"