#Задан целочисленный массив. Определить количество участков массива,
#на котором элементы монотонно возрастают (каждое следующее число больше предыдущего)
import random

N = int(input())
M = int(input())
array = []
count = 0
for _i in range(N):
    box = []
    for _j in range(M):
        item = random.randint(1, 9)
        box.append(item)
        if box[_j-1] < box[_j]:
            print(box[_j-1:_j+2])
            count += 1
    array.append(box)
print(array)
print(count)
