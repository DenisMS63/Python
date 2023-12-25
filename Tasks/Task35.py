# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def simple_digit(n):
    for divider1 in range(2, n):
        if n % divider1 == 0:
            return "no"
    return "yes"

def simple_digit_2(n):          #работает быстрее, делает намного меньше итераций
    for divider1 in range(2, int(n ** 0.5) + 1):
        if n % divider1 == 0:
            return "no"
    return "yes"

def simple_digit_3(n):          #работает быстрее, делает намного меньше итераций
    if n != 2 and n % 2 == 0:
        return "no"
    for divider1 in range(3, int(n ** 0.5) + 1, 2):
        if n % divider1 == 0:
            return "no"
    return "yes"

num = int(input("Введите число: "))
print(simple_digit(num))
print(simple_digit_2(num))
print(simple_digit_3(num))