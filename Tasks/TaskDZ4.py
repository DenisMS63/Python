# Определите, можно ли от шоколадки размером a × b долек отломить c долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# Выведите yes или no соответственно.

a = 8
b = 7
c = 156

# res = a * b

if c % b == 0 or c % a == 0 and a * b > c:
    print("yes")
else: print("no")

# if c % 2 == 0 and res % 2 == 0:
#     print("yes")
# else: print("no")
