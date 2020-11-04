st = input("Enter the number ")
a = len(st)
if a > 10:
    print(st+'!!!')
elif a < 10 :
    print(f"{st[1]} ")
else:
    print("длина равна 10 символов")
