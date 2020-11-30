"""Даны три слова. Выяснить, является ли хоть одно из них палиндромом
("перевертышем"), т. е. таким, которое читается одинаково слева направо и
справа налево. (Определить функцию, позволяющую распознавать слова
палиндромы.)"""

words = ['qwerty', 'texet', 'kolobok']


def Polindrom(a):
    for i in a:
        x = i[::-1]
        y = int(len(i) / 2)
        if i[0:y] == x[0:y]:
            print(f'{i} - polindrom')
        else:
            print(f'{i} - ne polindrom')


x = Polindrom(words)
