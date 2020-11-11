# С использованием цикла for
fibo = [1, 1]
i = 0
for i in range(13):
    fibo.append(fibo[i] + fibo[i+1])
print(fibo)
# С использованием цикла while
fibo = [1, 1]
i = 0
while i < 13:
    fibo.append(fibo[i] + fibo[i+1])
    i += 1
print(fibo)
