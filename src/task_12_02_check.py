from task_12_02 import Circle
from task_12_02 import Point
from task_12_02 import Triangle
from task_12_02 import Square


first_figure = Circle(1, 8, 3)
second_figure = Triangle(Point(1, 1), Point(4, 5), Point(7, 8))
third_figure = Square(Point(3,2), Point(9, 6))

list_of_figures = [first_figure, second_figure, third_figure]

new_list = [print(f'Perimetr_of_figure: {i.calculate_perimetr()}\n'f'Area_of_figure: {i.calculate_area()}')for i in list_of_figures]
