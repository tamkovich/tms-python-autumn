x = input()
y = len(x) / 2
z = str(y).split('.')
middle_symbol_number = int(z[0])
first_symbol = x[:1]
middle_symbol = x[middle_symbol_number-1:middle_symbol_number]

if z[1] != '0':
    if first_symbol == x[middle_symbol_number:middle_symbol_number+1]:
        print(x[:])
        print(x[:middle_symbol_number+1])
    else:
        print(x[middle_symbol_number])

elif z[1] == '0':
    if first_symbol == x[middle_symbol_number-1:middle_symbol_number]:
        print(x[:middle_symbol_number])
    else:
        print(x[middle_symbol_number-1])