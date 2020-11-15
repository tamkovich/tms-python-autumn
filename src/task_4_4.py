#Цикл For
n=int(input("vvedi dlinnu spiska: "))
x=list(range(1,n+1))
first=x[0]
for i in range(len(x)-1):
    x[i]=x[i+1]
x[len(x)-1]=first
print(x)

#Цикл While
n=int(input("vvedi dlinnu spiska: "))
x=list(range(1,n+1))
first=x[0]
i=0
while i <= len(x)-2:
    x[i]=x[i+1]
    i+=1
x[len(x)-1]=first
print(x)