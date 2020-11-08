a = float(input("enter coefficient a of quadratic equation: "))
b = float(input("enter coefficient b of quadratic equation: "))
c = float(input("enter coefficient c of quadratic equation: "))
d = b ** 2 - 4 * a * c
print("D = ", d)
if d > 0:
    x1 = (-b + d**0.5) / (2 * a)
    x2 = (-b - d**0.5) / (2 * a)
    print("real root of x1 = \n", x1, "\nreal root of x2= ", x2)
elif d == 0:
    x = -b / (2 * a)
    print("real root x = ", x)
else:
    print(" There are complex roots, but no real ") # i = -1**0.5
    real_part = -b / (2 * a)
    complex_part = (abs(d) ** 0.5)/(2*a)
    x1 = complex(real_part, complex_part)
    x2 = complex(real_part, -complex_part)
    print("complex root x1:\n",x1,"\n","complex root of x2:\n", x2)
