# В списке хранятся числа. Нужно выбрать только четные числа
# и составить список пар (число; квадрат числа) 

list1 = [1, 2, 3, 5, 8, 15, 23, 38]

# for el in list1:
#     if el % 2 == 0:
#         print(el)

# list2 = [f"{el}; {el ** 2}" for el in list1 if el % 2 == 0]
# print(list2)

# Решение преподавателя

res = list()

for i in list1:
    if i % 2 == 0:
        res.append((i, i ** 2))
print(res)