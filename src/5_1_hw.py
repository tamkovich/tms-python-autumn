while True:
    sign = input('Vvedite znak operacii(+, –, /, *): ')
    if sign == '0':
        break
    if sign in ('+', '-', '*', '/', ):
        x = float(input('x:'))
        y = float(input('y:'))
        if sign == '+':
            print('%.2f' % (x + y))
        elif sign == '-':
            print('%.2f' % (x - y))
        elif sign == '*':
            print('%.2f' % (x * y))
        elif sign == '/':
            if y !=0:
                print('%.2f' % (x / y))
            else:
                print('Na nol ne delyat')
    else:
        print('Nevernij!!!')