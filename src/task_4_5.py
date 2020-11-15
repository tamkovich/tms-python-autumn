#Цикл For
n=int(input("vvedi dlinnu spiska Fibonachi: "))
a=[1,1]
for i in range(n-2):
    a.append(a[i]+a[i+1])
print(a)

#Цикл While
n=int(input("vvedi dlinnu spiska Fibonachi: "))
a=[1,1]
i=0
while i <=n-3:
    a.append(a[i]+a[i+1])
    i+=1
print(a)



