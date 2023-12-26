# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

from random import randint

# size = int(input("Введите размер списка: "))
# list_1 = [randint(1, 5) for i in range(size)]

# print(list_1)
# count = 0
# for i in range(size - 1):
#     for j in range(i + 1, size):
#         if list_1[i] == list_1[j]:
#             count += 1        

# print(count)

size = int(input("Введите размер списка: "))
list_1 = [randint(1, 5) for i in range(size)]

print(list_1)

count = 0
for i in range(size - 1):
    count += list_1[i + 1:].count(list_1[i])

print(count)