import random

n = int(input("Введите кол-во дней: "))
count = 0
max_count = 0 

for i in range(n):
    temperature = random.randint(-50, 50)
    print(temperature, end = " ")
    if temperature > 0:
        count += 1
        if max_count < count:
            max_count = count
    else: 
        count = 0

print()
print(max_count)
    