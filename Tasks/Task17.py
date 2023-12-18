# Дан список чисел, определите сколько в нем
# находится различных чисел

from random import randint

size = int(input("Введите размер списка: "))

list_1 = [randint(-5, 5) for _ in range(size)]
print(list_1)
new_set = set(list_1)
print(new_set)
print(len(new_set))