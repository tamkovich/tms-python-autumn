import random

new_box = []
box = []
for i in range(1, 11):
    box.append(random.randint(1, 12))
print(box)
c = 0
l = 1
for j in range(1, len(box)):
    if box[j - 1] < box[j]:
        l+=1
    else:
        if l>1:
            c+=1
        l=1
if l > 1:
    c += 1
print(c)
