'''Создать класс Matrix.
Атрибуты - data(содержит саму матрицу - список списков), n, m.
Определить конструктор(с параметрами(передача размерности: n, m и диапазона случайных чисел: a, b), по-умолчанию
(матрица 5 на 5 где все элементы равны нулю), копирования) ,
переопределить магический метод str для красивого вывода.
Описать функции, которые принимают на вход объект класса Matrix. Функции позволяют искать максимальный элемент матрицы,
минимальный, сумму всех элементов.
Создать в файле main.py матрицу. Воспользоваться всеми описанными функциями и методами'''

from random import randint

class Matrix:
    def __init__(self, a: int, b: int, n: int = 5, m: int = 5) -> None:
        self.n = n
        self.m = m
        self._data: list[list] = None
        self.a = a
        self.b = b


    @property
    def data(self):
        self._data = [[randint(self.a, self.b) for _ in range(self.n)] for _ in range(self.m)]
        return self._data


    @data.setter
    def data(self, data):
        self._data = data

    def gen_default_matrix(self) -> None:
        """Сгенерировать матрицу по умолчанию (нулевую)"""
        self._data = [[0 for _ in range(self.n)] for _ in range(self.m)]

    def __str__(self) -> str:
        return f'{self._data[0]}' \
                f'\n{self._data[1]}' \
                f'\n{self._data[2]}' \
                f'\n{self._data[3]}' \
                f'\n{self._data[4]}'