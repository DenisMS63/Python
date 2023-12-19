# Дан массив из целых чисел. Программа подсчитывает кол-во эл-ов массива,
# больших предыдущего (эл-та с предыдущим номером)

array = [0, -1, 5, 2, 3] 
count = 0

for i in range(len(array) - 1):
    if array[i] < array[i + 1]:
        count += 1

print(count)

print(sum([1 for i in range(len(array) - 1) if array[i] < array[i + 1]]))