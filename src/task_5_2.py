number = 123
result = []
summa = 0
proiz = 1
while True:
    if number > 0:
        x = number % 10
        result.append(x)
        number //= 10
    else:
        break
for i in range(3):
    summa += int(result[i])
    proiz *= int(result[i])
print(summa, proiz)
