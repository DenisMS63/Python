# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числаN.
# n=16
# #Вывод
# 1
# 2
# 4
# 8
# 16

n = 3
k = 0
x = 0

while x < n:
    x = 2**k
    k += 1
    if x <= n:
        print(x)