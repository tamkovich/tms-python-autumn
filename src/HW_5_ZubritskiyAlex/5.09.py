#Для каждого натурального числа в промежутке от m до n вывести все делители,
#кроме единицы и самого числа. m и n вводятся с клавиатуры.

m = int(input())
n = int(input())
first_list = [i for i in range(m, n+1)]
for number in first_list:
    list_of_divider = []
    for divider in range(2, number-1):
        if number % divider == 0:
            list_of_divider.append(divider)
    print(number," : ",list_of_divider)
