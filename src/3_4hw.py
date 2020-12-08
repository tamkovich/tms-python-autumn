x = input('Type smthng: ')
y = len(x) // 2
z = x[y]
if z == x[0]:
    print(x[0:-1:])
else:
    print(x[y])