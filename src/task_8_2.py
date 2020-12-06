# Даны три слова. Выяснить, является ли хоть одно из них палиндромом
# ("перевертышем"), т. е. таким, которое читается одинаково слева направо и
# справа налево. (Определить функцию, позволяющую распознавать слова
# палиндромы.)


worlds = ["Deed", "Brother", "Level"]

for i in worlds:
    i = i.upper()
    if i == i[::-1]:
        print(i, "is palindrome")
    else:
        print(i, "is NOT palindrome")

print("-----------------------------")


def palindrome(world: str) -> str:
    """
    This method determines if the word is a palindrome

    :param world: any word
    :return: answer
    """
    if str(world) == str(world[::-1]):
        return "is palindrome"
    else:
        return "is NOT palindrome"


print(palindrome("hih"))
print(palindrome("hip-hop"))
