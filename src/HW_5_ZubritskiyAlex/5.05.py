#В массиве целых чисел с количеством элементов 19 определить максимальное число и
#заменить им все четные по значению элементы.

array = [1, 32, 44, 78, 93, 15, 74, 88, 61, 45, 25, 14, 16, 55, 18, 89, 93, 81, 49]
value_of_max = max(array)
for _i in range(len(array)):
    if array[_i] % 2 == 0:
        array[_i] = value_of_max
print(array)
