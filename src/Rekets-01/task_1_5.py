# Даны катеты прямоугольного треугольника. Найти его гипотенузу и
# площадь.

a = float(input('First leg: '))
b = float(input('Second leg: '))

# Найти его гипотенузу:
hypotenuse = pow((a**2+b**2),(1/2))
print('hypotenuse: ', hypotenuse)

# Площадь:
area = a*b*(1/2)
print('area: ', area)
