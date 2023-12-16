import random

num = int(input("Введите кол-во чисел: "))

min_num = 0
max_num = 1000

for i in range(num):
    current_num = random.randint(1, 10)
    print(current_num, end = " ")
    if max_num < current_num:
        max_num = current_num
    if min_num > current_num:
        min_num = current_num

print()
print(min_num, max_num)