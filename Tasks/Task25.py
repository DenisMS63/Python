# Программа принимает на вход строку и отслеживает сколько раз каждый символ 
# уже встречался. Кол-во повторов добавляется к символам с помощью 
# постфикса формата _n .

# text = "a a a b c a a d c d d"
# list_symbols = text.split()         #список
# unique_text = set(list_symbols)     #множество
# uniq_symb = dict()

# for symbol in list_symbols:
#     if symbol not in uniq_symb:
#         uniq_symb[symbol] = 0
#         print(symbol, end = " ")
#     else:
#         uniq_symb[symbol] += 1
#         # print(symbol, uniq_symb[symbol], sep = "_" )
#         print(f"{symbol}_{uniq_symb[symbol]}", end = " ")


# print(text)
# print(list_symbols)
# print(unique_text)
# print(uniq_symb)
        

# Второе решение
text = "a a a b c a a d c d d"
list_symbols = text.split()         #список
unique_text = set(list_symbols)     #множество
uniq_symb = dict()
print()
result = ""

for symbol in list_symbols:
    if symbol not in uniq_symb:
        # uniq_symb[symbol] = 0
        result += f"{symbol} "
    else:
        # uniq_symb[symbol] += 1
        # print(symbol, uniq_symb[symbol], sep = "_" )
        result += f"{symbol}_{uniq_symb[symbol]} "
    uniq_symb[symbol] = uniq_symb.get(symbol, 0) + 1

print(result.strip())