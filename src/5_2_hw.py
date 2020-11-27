n = int(input('Введите число: '))
summ = 0
mult = 1

while n > 0:
    digit = n % 10  #таким образом получаю остаток от деления
    summ = summ + digit
    mult = mult * digit
    n = n // 10 #таким образом от остатка избавляюсь, получается.
print(summ)
print(mult)