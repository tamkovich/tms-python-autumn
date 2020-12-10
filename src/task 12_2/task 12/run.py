from paket.classes import task_12_2_classes

circle = task_12_2_classes.Circle(2, task_12_2_classes.Point(3, 2))

triangle = task_12_2_classes.Triangle(
    task_12_2_classes.Point(2, 1), task_12_2_classes.Point(2, 4), task_12_2_classes.Point(6, 1)
)

squad = task_12_2_classes.Square(task_12_2_classes.Point(0, 0), task_12_2_classes.Point(2, 3))

li = [circle, triangle, squad]
for i in li:
    print(f"площадь {i} = {i.find_square()}")
    print(f"периметр {i} = {i.find_perimeter()}")