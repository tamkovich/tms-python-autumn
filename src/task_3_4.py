a = input("Введи строку ")
b = int(len(a))
c = int(b/2)
if b > (c*2):
  print(a[c])
  x = a[c]
else:
  print(a[c-1])
  x = a[c-1]
if x == (a[0]):
  y = a[1:(b-1)]
  print(y)