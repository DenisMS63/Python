# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# 1

list_1 = [1, 2, 3, 4, 5, 1, 1]
n = int(input("Введите число для поиска: "))
# count = 0

# for i in list_1:
#     if n == i:
#         count += 1

# print(count)

count = 0
for i in range(len(list_1)):
    if list_1[i] == n:
        count += 1
print(count)