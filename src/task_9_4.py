#Создать универсальный декоратор, который меняет порядок аргументов в
#функции на противоположный.
import random
list_1 = [random.randint(0,1000) for i in range(20)]
def decorator(func):
    def reversion(*args):
        return list(reversed(*args))
    return reversion
@ decorator
def revers():
    pass

print(list_1)
print(revers(list_1))