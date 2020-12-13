'''Создать класс Matrix.
Атрибуты - data(содержит саму матрицу - список списков), n, m.
Определить конструктор(с параметрами(передача размерности: n, m и диапазона случайных чисел: a, b), по-умолчанию
(матрица 5 на 5 где все элементы равны нулю), копирования) ,
переопределить магический метод str для красивого вывода.
Описать функции, которые принимают на вход объект класса Matrix. Функции позволяют искать максимальный элемент матрицы,
минимальный, сумму всех элементов.
Создать в файле main.py матрицу. Воспользоваться всеми описанными функциями и методами'''

from .matrix_classes import Matrix

def find_max_matrix_element(matrix: Matrix) -> int or float:
    max_element = matrix.a
    for i in matrix._data:
        if max_element < max(i):
            max_element = max(i)
    return max_element


def find_min_matrix_element(matrix: Matrix) -> int or float:
    min_element = matrix.a
    for i in matrix._data:
        if min_element > min(i):
            min_element = min(i)
    return min_element


def find_sum_matrix_elements(matrix: Matrix) -> int or float:
    summa = 0
    for i in matrix._data:
        summa += sum(i)
    return summa
