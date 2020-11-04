x =input("Введите строку")
y = len(x)
z = y/2
if y%2==0:
    print(x[int(z)-1:int(z)])
elif y%2!=0:
    print(x[int(z)])
if x[int(z)]== x[0]:
    print(x[1:-1])



