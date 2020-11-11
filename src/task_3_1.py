#Введите число. Если это число делиться на 1000 без остатка, то выведите на
#экран "millennium"

number = int(input())
ans = number % 1000
if ans == 0:
    print("millennium")
else:
    print("error")
