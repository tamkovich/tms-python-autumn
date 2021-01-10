"""Выполнить задание 1 с использованием класса Math. Класс принимает в
качестве аргументов два числа. Определить 4 метода(сложение,
вычитание, умножение, деление). Добавить валидацию входных данных.
Программа должна состоять из четырех файлов(main.py, classes.py,
ui_func.py exceptions.py)"""


class Math:
    def __init__(self, a, b: float):
        self.a = a
        self.b = b

    def summa(self) -> float:
        return self.a + self.b

    def deduction(self) -> float:
        return self.a - self.b

    def mult(self) -> float:
        return self.a * self.b

    def div(self) -> float:
        return self.a / self.b
