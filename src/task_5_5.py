import random

new_box = []
box = []
for i in range(19):
    box.append(random.randint(1, 12))
print(box)
for j in box:
    if j % 2 == 0:
        new_box.append(max(box))
    else:
        new_box.append(j)
print(new_box)
