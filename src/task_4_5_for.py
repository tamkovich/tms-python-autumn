# Составить список чисел Фибоначчи содержащий 15 элементов.

i = 0
a = 1
count = 0

for count in range(0, 15):
    f = i + a
    i = a
    a = f
    count += 1
    print(f, end=(" "))
