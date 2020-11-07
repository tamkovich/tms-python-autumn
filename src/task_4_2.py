#Цикл For
n=int(input("vvedi dlinnu spiska: "))
x=list(range(1,n+1))
ctr=0
z=list()
for i in range(len(x)):
    if x[i]%2==0:
        z.append(x[i])
        ctr+=1
print(z)
print(f"kolichestvo chetnih chisel: {ctr}")

#Цикл While
n=int(input("vvedi dlinnu spiska: "))
x=list(range(1,n+1))
ctr=0
z=list()
g=0
while g <=len(x)-1:
    if x[g]%2==0:
        z.append(x[g])
        ctr+=1
        g+=1
    else:
        g+=1
        

print(z)
print(f"kolichestvo chetnih chisel: {ctr}")