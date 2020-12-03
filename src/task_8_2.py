def polindrom(*args):
    """This function calculates whether a word is a palindrome"""
    for i in args:
        if i == i[::-1]:
            print(f"word {i} is polindrom ")
        else:
            print(f"word {i} is not polindrom")


polindrom("qweewq", "qwerty", "ooo")
