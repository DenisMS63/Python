# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо
# var1 = '5 4' # количество элементов первого и второго множества
# var2 = '1 3 5 7 9' # элементы первого множества через пробел
# var3 = '2 3 4 5' # элементы второго множества через пробел
# На выходе 3 5

var1 = '5 4' 
var2 = '1 2 3' 
var3 = '1 2 3 4'

list_var2 = var2.split()
list_var3 = var3.split()

sorted_list_var2 = sorted(list_var2)
sorted_list_var3 = sorted(list_var3)

set_var2 = set(sorted_list_var2)
set_var3 = set(sorted_list_var3)

new_intersection = set_var2.intersection(set_var3)

out = sorted(list(new_intersection))

# print(sorted_list_var2)
# print(sorted_list_var3)
for i in out:
    print(i, end=" ")


