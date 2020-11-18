#Цикл For
n=int(input("vvedi dlinnu spiska: "))
x=list(range(1,n+1))
z=list()
for i in range(len(x)):
    z.append(x[i]*2)
print(z)

#Цикл While
y=int(input("vvedi dlinnu spiska: "))
w=list(range(1,y+1))
c=list()
i=0
while i <=len(w)-1:
    c.append(x[i] * 2)
    i+=1
print(c)
