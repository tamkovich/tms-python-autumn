x = int(input("введите число старта массива : "))
massiv = list(range((x),(x + 10)))
print("массив:", massiv)
count = 0
i = 0
while i < (len(massiv) - 1):
    if massiv[i] < massiv[i + 1]:
        count += 1
    i += 1
print(count)
