# В списке хранятся числа. Нужно выбрать только четные числа
# и составить список пар (число; квадрат числа) 

# list1 = [1, 2, 3, 5, 8, 15, 23, 38]

# for el in list1:
#     if el % 2 == 0:
#         print(el)

# list2 = [f"{el}; {el ** 2}" for el in list1 if el % 2 == 0]
# print(list2)

# Решение преподавателя

# res = list()

# for i in list1:
#     if i % 2 == 0:
#         res.append((i, i ** 2))
# print(res)

# Решение через Лямбда функции

def select(f, col):     # map()
    return[f(x) for x in col]

def where(f, col):      # filter()      
    return [x for x in col if f(x)]

list1 = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, list1)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x ** 2), res))  # ф-я Лямбда возвращает кортеж (круглые скобки) из эл-тов Х и квадрата Х, 
                                                # после этого ф-я select преобразуется в список ф-ей list
print(res)