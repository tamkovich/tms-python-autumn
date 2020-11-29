# Создать универсальный декоратор, который меняет порядок аргументов в
# функции на противоположный.

def decorator(real_order):
    def fake_order(*args: tuple):
        list_args = list(args)
        list_args.reverse()
        args = tuple(list_args)
        return real_order(*args)
    return fake_order


@decorator
def order(*args: tuple):
    return args


print(order(1, 2, 3, 4))
