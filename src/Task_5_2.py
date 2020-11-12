""" Дано число. Найти сумму и произведение его цифр."""

x = list(str(input("Введите число: ")))
_mult = 1
_sum = 0
for i in range(len(x)):
    a = x.pop()
    _mult = int(a)*_mult
    _sum += int(a)
print("Sum: ", _sum)
print("Multiplication: ", _mult)
