from math import sqrt
a = int(input("a"))

b = int(input("b"))
c = int(input("c"))

print(str(a)+" x2 " + str(b)+ " x " + str(c) + " = 0" )

D = b**2 - 4*a*c
print("D = "+str(D))
if D > 0 :
    x1 = (-b + sqrt(D)) / 2 * a
    print(x1)
    x2 = (-b - sqrt(D)) / 2 * a
    print(x2)
elif D == 0:
    x1 = (-b ) / 2 * a
    print(x1)
else :
    print("нет корней ")
