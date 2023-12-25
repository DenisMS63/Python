def suma_num(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    print(summa)

suma_num(5)

#######################################################

for (index, element) in enumerate("Hello"):
    print(index, element, sep=" is ",end=" | ")