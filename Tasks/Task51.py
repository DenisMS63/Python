# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by(characteristic, objects):
#     if not objects:
#         return True
#     print(*map(characteristic, objects))
#     return all(map(characteristic, objects))

# values = [0, 2, 10, 6] 

# if same_by(lambda x: x % 2 == 0, values):
#     print("same")
# else:
#     print("different")

# РЕШЕНИЕ 2
    
def same_by(characteristic, objects):
    if not objects:
        return True
    print(set(map(characteristic, objects)))
    return len(set(map(characteristic, objects))) == 1      # если все True, то множество будет равно 1 (только True), иначе будет равно 2 (True и False)

values = [0, 2, 10, 6] 

if same_by(lambda x: x % 2 == 0, values):
    print("same")
else:
    print("different")