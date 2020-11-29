number = input('Введите число: ')
if number.isdigit() == True:
    number = int(number)
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
else:
    print('Введен не верный тип данных')
