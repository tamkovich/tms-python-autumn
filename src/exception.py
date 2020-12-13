def exceptn():
    while True:
        x = input()
        if x.isdigit():
            x = int(x)
            return x
        else:
            print('Это не числовое значение введите числовое')
            continue
