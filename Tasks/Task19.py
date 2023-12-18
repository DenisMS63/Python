# Дана последовательность из N целых чисел и число К.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на К элементов вправо, К - положительное число.
# [1, 2, 3, 4, 5] k = 3
# [3, 4, 5, 1, 2]

from random import randint

list_1 = [i for i in range(1, randint(7, 10))]
print(list_1)
n = int(input("Введите кол-во сдвигов: "))

for i in range(n):
    last_num = list_1.pop()
    list_1.insert(0, last_num)

print(list_1)

# Срезы
# print(list_1[-n:] + list_1[:-n])

# print(list_1[-n:])
# print(list_1[:-n])
# print()
# print(list_1[n:])
# print(list_1[:n])