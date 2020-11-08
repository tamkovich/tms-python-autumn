from math import fabs
x = int(input("input x "))
y = int(input("input y "))
a = (fabs(x)-fabs(y))/(1+fabs(x*y))
print("result"+str(a))
