x = input("vvedite chislo:")
summa = 0
mult = 1
for i in x:
    summa += int(i)
    mult *= int(i)
print(f"summa chisel ishodnogo chisla: {summa}")
print(f"proizvedenie chisel ishodnogo chisla: {mult}")