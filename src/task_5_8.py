stroka = input("vvedite stroku: ")
spisok = stroka.split()
reversed_str = []
for i in range(len(spisok)):
    reversed_str.append(spisok[(len(spisok) - 1) - i])
print(reversed_str)