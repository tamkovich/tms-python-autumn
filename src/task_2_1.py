#Создать строку равную третьему символу введенной строки.

stroka = str(input())
_len = len(stroka)
if _len >= 3:
    print(stroka[2])
if _len < 3:
        print('error')
