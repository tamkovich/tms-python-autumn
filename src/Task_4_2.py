import random
# Выполнение с циклом for
n = int(input("Введите длинну списка: "))
list1 = random.sample(range(100), n)
x = 0
for i in list1:
    if i % 2 == 0:
        x += 1
print(list1)
print(x)

# Выполнение с циклом while
n = int(input("Введите длинну списка: "))
list1 = random.sample(range(100), n)
print(list1)
i = 0
x = 0
y = 0
while list1:
    y = list1.pop()
    if y % 2 == 0:
        x += 1
    i += 1
print(x)
