from matrix_utils import matrix_classes
from matrix_utils import matrix_funcs


if __name__ == "__main__":
    matrix = Matrix(3, 4)
    matrix.data
    print(matrix_funcs.find_max_matrix_element(matrix))
    print(matrix_funcs.find_min_matrix_element(matrix))
    print(matrix_funcs.find_sum_matrix_elements(matrix))