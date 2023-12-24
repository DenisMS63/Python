# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint
n = int(input("Введите кол-во оценок: "))
list_1 = [randint(1, 5) for i in range((n))]
print(list_1)
max_bal = max(list_1)
min_bal = min(list_1)

for i in range(len(list_1)):
    if list_1[i] == max_bal:
       list_1[i] = min_bal

print(list_1)