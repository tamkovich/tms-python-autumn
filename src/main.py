from .task2 import classes

circle = classes.Circle(2, classes.Point(3, 2))

triangle = classes.Triangle(
    classes.Point(2, 1), classes.Point(2, 4), classes.Point(6, 1)
)

squad = classes.Square(classes.Point(0, 0), classes.Point(2, 3))

li = [circle, triangle, squad]
for i in li:
    print(f"площадь {i} = {i.find_square()}")
    print(f"периметр {i} = {i.find_perimeter()}")
