x = int(input("введите число старта массива : "))
massiv = list(range((x),(x + 19)))
new_massiv = list()
print("массив:", massiv)
max_dig = max(massiv)
print ("максимальное число массива :", max_dig)
for i in range(len(massiv)):
    if massiv[i] % 2 == 0:
        new_massiv.append(massiv[i])
        massiv[i] == max_dig
print("Новый массив:", new_massiv)
