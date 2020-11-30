# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.

def decorator(func):
    def wrapper(arg):
        new_arg = [a for a in arg if a % 2]
        return func(new_arg)
    return wrapper

@decorator
def function(x):
    print(x)

function([1,12,13,14,16,18,66,13,15,14])