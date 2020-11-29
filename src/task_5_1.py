while True:
    X = input('Введите первое значение: ')
    Y = input('Введите второе значение: ')
    if X.isdigit() == True and Y.isdigit() == True:
        X = int(X)
        Y = int(Y)
    else:
        print('Введены не числа')
        break
    sign = input('Введите знак: ')
    if sign == '+':
        print(X + Y)
    elif sign == '-':
        print(X - Y)
    elif sign == '*':
        print(X * Y)
    elif sign == '/' and Y != 0:
        print(X / Y)
    elif sign == '/' and Y == 0:
        print('Деление на 0. Введите другое значение Y.')
    elif sign == '0':
        print('Конец программы.')
        break
    else:
        print('Неверный знак! Введите +, -, *, /, 0')
        continue
