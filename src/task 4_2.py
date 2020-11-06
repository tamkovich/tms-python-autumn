#Дан список целых чисел. Подсчитать сколько четных чисел в списке
import random
length_of_list = int(input("Enter the length of list "))
first_list = random.sample(range(100), length_of_list)
print("first list: \n ", first_list)
even = len([i for i in first_list if i % 2 == 0])
print("number of even elements: \n",even)
even = 0
i = 0
while first_list:
    x = first_list.pop()
    if x % 2 == 0:
        even += 1
    i += 1
print("number of even elements from while : \n",even)
