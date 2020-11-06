stroka = input("Enter the str")
a = len(stroka)
middle = int(a / 2)
if a % 2 == 0:
    print(stroka[middle-1])
elif stroka[0] == stroka[middle]:
    print(stroka[1:a-1])
else:
    print(stroka[middle])
