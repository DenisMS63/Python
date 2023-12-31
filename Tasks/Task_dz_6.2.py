# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент a1, разность d и количество элементов n 
# будет задано автоматически. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# На входе:
# a1 = 2
# d = 3
# n = 4
# На выходе:
# 2
# 5
# 8
# 11

a1 = 2
d = 3
n = 4

list_1 = []
list_1.insert(0, a1)

for i in range(1, n):
    list_1.insert(i, list_1[i - 1] + d)

for el in list_1:
    print(el)