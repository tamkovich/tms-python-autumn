def get_valid_int_number():
    """Функция, что проверяет, было ли на входе принято число."""
    while True:
        x = input()
        if x.isdigit():
            x = int(x)
            return x
        else:
            print('It is not integer. Put another value:')
