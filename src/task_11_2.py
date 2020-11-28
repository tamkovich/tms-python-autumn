"""Создать класс Car. Атрибуты: марка, модель, год выпуска,
скорость(по умолчанию 0). Методы: увеличить скорости
(скорость + 5), уменьшение скорости(скорость - 5), стоп
(сброс скорости на 0),отображение скорости, разворот
(изменение знака скорости). Все атрибуты приватные."""


class Car:
    """Class car.

    The constructor takes a mark, model, year_of_issue, speed.
    """
    def __init__(self, mark, model, year_of_issue, speed=0):
        """Object initialization."""
        self.__mark = mark
        self.__model = model
        self.__year_of_issue = year_of_issue
        self.__speed = speed

    def increase_speed(self):
        """Increases speed."""
        self.__speed += 5

    def decrease(self):
        """Decreases speed."""
        self.__speed -= 5

    def stop(self):
        """Stops speed."""
        self.__speed = 0

    def show_speed(self):
        """Show speed."""
        print(self.__speed)

    def reversal(self):
        """Reverses sign."""
        self.__speed = -self.__speed


car = Car("bmw", "e30", 2007)
car.increase_speed()
car.increase_speed()
car.show_speed()
car.decrease()
car.show_speed()
car.reversal()
car.show_speed()
car.stop()
car.show_speed()
