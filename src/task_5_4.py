# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.

N = int(input('N = '))
a = 0
s = 0

for i in range(1, N + 1):
    a = 1 / i
    s += a
print('summa = ', s)
