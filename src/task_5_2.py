"""Дано число. Найти сумму и произведение его цифр."""


print("Vvedite chislo")
n = input()
if n.isdigit():
    n = int(n)

summ = 0
umnozh = 1

while n > 0:
    ostatok = n % 10
    summ = summ + ostatok
    umnozh *= ostatok
    n //= 10

print("Summ:", summ)
print("Umnozhenie:", umnozh)
