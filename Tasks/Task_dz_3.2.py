# Требуется найти в массиве list_1 самый близкий 
# по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. 
# Если значение k совпадает с этим элементом - выведите его.
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

list_1 = [2, 4, 1, 6, 8, 2, 9, 2, 5]
k = int(input("Введите число для поиска: "))

max_list_1 = max(list_1)
num = 0

for i in list_1:
    diff = abs(i - k)
    if diff < max_list_1:
        num = i
        max_list_1 = diff

print(num)   
    



