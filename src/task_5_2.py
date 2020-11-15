"""Дано число. Найти сумму и произведение его цифр."""
while True:
    number = input("enter number ")
    if len(number) == 1:
        print("number consist of one digit")
        continue
    elif number.startswith("-"):
        continue
    else:
        break
summma = 0
composition = 1
for i in number:
    summma += int(i)
    composition *= int(i)
print(f"sum = {summma} composition = {composition} ")
