'''Создать класс Matrix.
Атрибуты - data(содержит саму матрицу - список списков), n, m.
Определить конструктор(с параметрами(передача размерности: n, m и диапазона случайных чисел: a, b), по-умолчанию
(матрица 5 на 5 где все элементы равны нулю), копирования) ,
переопределить магический метод str для красивого вывода.
Описать функции, которые принимают на вход объект класса Matrix. Функции позволяют искать максимальный элемент матрицы,
минимальный, сумму всех элементов.
Создать в файле main.py матрицу. Воспользоваться всеми описанными функциями и методами'''

from matrix_utils import matrix_classes
from matrix_utils import matrix_funcs


if __name__ == "__main__":
    matrix = matrix_classes.Matrix(3, 10)
    matrix.data = [[2,3,4,5,6],[6,5,4,5,7],[11,2,5,1,9],[10,6,3,9,12],[13,3,6,8,0]]# задать матрицу (любую для теста)
    print(matrix_funcs.find_max_matrix_element(matrix))
    print(matrix_funcs.find_min_matrix_element(matrix))
    print(matrix_funcs.find_sum_matrix_elements(matrix))