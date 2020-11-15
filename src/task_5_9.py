"""Для каждого натурального числа в промежутке от m до n вывести все делители,
кроме единицы и самого числа. m и n вводятся с клавиатуры.
Пример:m =100, n = 105"""
m = int(input("enter min number of range: "))
n = int(input("enter max number of range: "))
new_list = list(range(m, n + 1))
result_list = list()
print(new_list)
for elem in new_list:
    for y in range(2, elem // 2 + 1):
        if elem % y == 0:
            if y not in result_list:
                result_list.append(y)
    print(elem, result_list)
    result_list = []
