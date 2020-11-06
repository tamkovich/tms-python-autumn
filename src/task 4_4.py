first_list = [1, 2, 3, 4, 5]
steps = 4
for i in range(steps):
    first_list.append(first_list.pop(0))
print("first_list from for: ", first_list)
first_list = [1, 2, 3, 4, 5]
while steps > 0:
    first_list.append(first_list.pop(0))
    steps -= 1
print("first_list from while: ", first_list)
