first_number = second_number = 1
fib_list = [1, 1]
n = int(input("enter length of list "))
if n < 2:
    print("enter more than two numbers ")

for i in list(range(2, n)):
    first_number, second_number = second_number, first_number + second_number
    fib_list.append(second_number)
print("fib_list with for: ", fib_list)

i = 0
fib_list_while = [1, 1]
fib1 = fib2 =1
while n-2 > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1
    fib_list_while.append(fib2)
print("fib_list with while: ", fib_list_while)
