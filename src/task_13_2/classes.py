"""Выполнить задание 1 с использованием класса Math. Класс принимает в
качестве аргументов два числа. Определить 4 метода(сложение,
вычитание, умножение, деление). Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, classes.py,
ui_func.py exceptions.py)."""


class Math:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def summa(self) -> int:
        return self.a + self.b

    def subtraction(self) -> int:
        return self.a - self.b

    def multiplication(self) -> int:
        return self.a * self.b

    def division(self) -> float:
        return self.a / self.b