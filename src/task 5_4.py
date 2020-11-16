n = int(input("введите целое число N: "))
summa = 1
for i in range(2, n+1):
    summa += 1/i
    print(i)
print(summa)
