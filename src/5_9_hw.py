# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105

m = int(input('Vvedi chislo: '))
n = int(input('Vvedi chislo bolshe pervogo: '))
x = range(m, n)
for i in x:
    for j in range(2, i - 1):
        if i % j == 0:
            print("Chislo", i, "Delitel", j)