# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

def sum_dividers(num):
    sum_divs = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divs += i
    return sum_divs

size = int(input("Введите предельное число: "))
# print(sum_dividers(size))

for num1 in range(1, size):
    for num2 in range(1, size):
        if sum_dividers(num1) == num2 and sum_dividers(num2) == num1 and num1 < num1:
            print(num1, num2)