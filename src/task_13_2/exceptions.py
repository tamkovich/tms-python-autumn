def exception_():
    """Проврерям число на целостность"""
    while True:
        x = input()
        if x.isdigit():
            x = int(x)
            return x
        else:
            print('Введено не целое число. Введите новое значение:')
