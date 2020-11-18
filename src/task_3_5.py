a = int(input("Введите a:"))
b = int(input("Введите b:"))
c = int(input("Введите c:"))
D=b**2 - 4*a*c
if D < 0:
  print("Нет действительных корней!")
elif D == 0:
  print("Один действительный корень: ")
  x = (b/(-2*a))
  print(x)
else:
  x = (-b+D**1/2) / (2*a)
  y = (-b-D**1/2) / (2*a)
  print("x1 =", x)
  print("x2 =", y)