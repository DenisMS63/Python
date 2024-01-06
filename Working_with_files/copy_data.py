import shutil

def copy_data():
    
    
    command = -1
    while command != "3":
        print("\nКопирование данных:\n"
              "1. Копирование по выбору\n"
              "2. Копировать все данные\n"
              "3. Завершить копирование\n")
        command = input("Выберите действие по номеру: ")
        print()

        match command:
            case "1":
                pick_copy()
            case "2":
                all_copy()
            case "3":
                print("Копирование успешно завершено!")

def pick_copy():
    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        list_contact = file.read().rstrip().split("\n\n")
        for contact in enumerate(list_contact, 1):
            print(*contact)
            print()

    user_pick = int(input("Введите номер карточки для копирования: ")) - 1      # так как эл-ты в списке нач-ся с нуля, а при выборе минимальное значение 1
    
    while  user_pick not in range(len(list_contact)):
        print("ОШИБКА: некорректное значение!")
        user_pick = int(input("Введите номер карточки для копирования: ")) - 1
        print()

    with open("phonebook_copy.txt", "a", encoding="UTF-8") as file:
        file.write(f"\n{list_contact[user_pick]}")

def all_copy():
    shutil.copy("phonebook.txt", "phonebook_copy.txt")
    print("Копирование всех данных успешно завершено!")