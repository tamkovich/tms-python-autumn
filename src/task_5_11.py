# Написать игру. Пользователь должен угадать число.
# Сперва вводиться диапазон угадывания. После колличество попыток.
# В случае правильного ответа - выводить You are the winner.
# В случае неправильного давать игроку подсказку(больше или меньше искомое число).
# Если за указанное количество попыток число не угадано - выводить: You are the loser и правильное число.

import random

print("Nuzhno ugadat' zagadannoe chislo!")
n = int(input("vvedite nachalo diapazona chisel: "))
m = int(input("vvedite konec diapazona chisel: "))
a = random.randint(n, m + 1)
while True:
    b = int(input("vvedite kolichestvo shansov: "))
    while b:
        c = int(input("vvedite vashe chislo: "))
        if c == a:
            print(f"You are the winner!!! {a}")
            break
        elif c != a:
            print(f"ne ugadali, poprobuite escho raz!")
            if c > a:
                print("zagadonnoe chislo men'she vvodimogo")
            else:
                print("zagadonnoe chislo bol'she vvodimogo")
        b -= 1
        print("ostalos' shansov - ", b)
    print(f"You are the loser!!!, pravil'noe chislo: {a}")
    break
