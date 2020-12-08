from matrix_classes import Matrix


def find_max_matrix_element(matrix: 'Matrix') -> int or float:
    max_element = matrix.a
    for i in matrix._data:
        if max_element < max(i):
            max_element = max(i)
    return max_element

def find_min_matrix_element(matrix: 'Matrix') -> int or float:
    min_element = matrix.a
    for i in matrix._data:
        if min_element > min(i):
            min_element = min(i)
    return min_element

def find_sum_matrix_elements(matrix: 'Matrix') -> int or float:
    summa = 0
    for i in matrix._data:
        summa += sum(i)
    return summa

