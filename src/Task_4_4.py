import random
# С использованием цикла while
n = int(input("Введите длинну списка: "))
list1 = random.sample(range(100), n)
print(list1)
b = []
i = 0
while i < len(list1):
    b.insert(i, list1[i-1])
    i += 1
print(b)
# С использованием цикла for
n = int(input("Введите длинну списка: "))
list1 = random.sample(range(100), n)
print(list1)
b = []
i = 0
for i in range(len(list1)):
    b.insert(i, list1[i-1])
print(b)
