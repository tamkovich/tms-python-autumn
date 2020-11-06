import random
length_of_list = int(input("Enter the length of list "))
first_list = random.sample(range(100), length_of_list)
print("first list: \n ", first_list)
second_list = [i * -2 for i in first_list]
print("second list: \n ", second_list)
i = 0
my_list = [1, 4, 9, 66, 17]
my_new_list = []
while first_list:
    my_new_list.append(my_list[i] * -2)
    i += 1
print("first list from while: \n ", my_list)
print("second list from while: \n ", my_new_list)
