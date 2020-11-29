""" Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных -
удалять все четные элементы из списка. """


def numbers():
    eval_numbers_list = []

    def func(*args):
        for i in args:
            if i % 2 != 0:
                eval_numbers_list.append(i)
        return eval_numbers_list

    return func


eval_numbers = numbers()

print(eval_numbers(1, 3, 4, 6, 4, 3, 23, 43))
