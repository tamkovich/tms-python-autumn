n = int(input("введите число : "))
summa = 0
multi = 1
while n > 0:
    x = n % 10
    summa = summa + x
    multi = multi * x
    n = n // 10         # деление нацело
print("Сумма:", summa)
print("Произведение:", multi)
