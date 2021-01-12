'''Выполнить задание 1 с использованием класса Math. Класс принимает в
качестве аргументов два числа. Определить 4 метода(сложение,
вычитание, умножение, деление). Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, classes.py,
ui_func.py exceptions.py).'''


class Math:
    def __init__(self, a: int, b: int) -> int:
        self.a = a
        self.b = b

    def summa(self):
        return self.a + self.b

    def subtraction(self,):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b
