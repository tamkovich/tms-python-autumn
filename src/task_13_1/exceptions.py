def exception_():
    while True:
        x = input()
        if x.isdigit():
            x = int(x)
            return x
        else:
            print('Введено не целое число. Введите новое значение:')
            continue
