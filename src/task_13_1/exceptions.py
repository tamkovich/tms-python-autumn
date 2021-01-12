def get_valid_int_value():
    """Проверяем целое ли число введено, и меняем тип данных"""
    while True:
        x = input()
        if x.isdigit():
            x = int(x)
            return x
        else:
            print('Введено не целое число. Введите новое значение:')
