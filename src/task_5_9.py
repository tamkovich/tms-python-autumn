# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105
# 100: 2 4 5 10 20 25 50
# 101:
# 102: 2 3 6 17 34 51
# 103:
# 104: 2 4 8 13 26 52
# 105: 3 5 7 15 21 35

m = int(input('m = '))
n = int(input('n = '))

for i in range(m, n + 1):
    print(i, ':', end=" ")
    for j in range(2, int(n / 2 + 1)):
        numbers = []
        ostatok = i % j
        #        print(i, "%", j, "=", x)
        if ostatok == 0:
            numbers.append(j)
            print(numbers, end=" ")
    print()
