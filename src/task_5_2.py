print("Vvedite chislo")
n = int(input())

summ = 0
umnozh = 1

while n > 0:
    ostatok = n % 10
    summ = summ + ostatok
    umnozh = umnozh * ostatok
    n = n // 10

print("Summ:", summ)
print("Umnozhenie:", umnozh)
