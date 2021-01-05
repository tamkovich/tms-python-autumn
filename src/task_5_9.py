"""9) Для каждого натурального числа в промежутке
от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с
клавиатуры."""


print("vvedite pervoe chislo")
m = int(input())
print("vvedite vtoroe chislo")
n = int(input())

for g in range(m, n + 1):
    print(g, ": ", end="")
    for i in range(2, g):
        if g % i == 0:
            print(i, end=" ")
    print("")
