#Дан список целых чисел. Подсчитать сколько четных чисел в списке

count = 0
for i in range(0, 11):
    if i % 2 != 0:
        continue
    count += 1
print(count)
