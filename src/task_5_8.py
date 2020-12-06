"""В заданной строке расположить в обратном порядке все слова.
 Разделителями слов считаются пробелы."""
string = input("enter string ")
x = string.split(" ")
print(x)
x.reverse()
print(x)
