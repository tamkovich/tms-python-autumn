x = int(input("vvedite chislo N: "))
summa = 0
for i in range(1,x+1):
    summa +=1/i
print(f"S=1+1/2+1/3+1/4+...+1/N: {summa}")
