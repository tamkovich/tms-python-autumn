# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.

def decorator1(_):
    def list2(*args: tuple):
        y = []
        for i in args:
            if i % 2 != 0:
                y.append(i)
        return y
    return list2


@decorator1
def list1(*args: tuple):
    return args


print(list1(1, 2, 3, 4, 5, 6, 7, 8))
