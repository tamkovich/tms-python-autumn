class Pet:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def get_age(self):
        return self.__age

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height

    def set_age(self):
        self.__age = age

    def set_weight(self):
        self.__weght = weight

    def set_height(self):
        self.__height = height

class Dog(Pet):
    def bark(self):
        print('Woof')

    def run(self):
        print('RUNRUNRUN')

class Cat(Pet):
    def voice(self):
        print('MEOW')

    def awful(self):
        print('KITTY SIT AMET SHED EVERYWHERE EAT THE GRASS SNIFF')

class Cow(Pet):
    def voice(self):
        print('MOOOOO')

    def extract(self):
        print('TAKE A BUCKET OF MILK YOU LASY SONOFABITCH')

class Parrot(Pet):
    def fly(self):
        if self.__weight > 7:
            print('THISS PARROT CANNOT FLY')
        else:
            print('FLYFLYFLYF')

    def seeds(self):
        print('THIS LITTLE SHITFAG COWARDLY STEALS ALL THE SEEDS AND NUTS IN TOWN!11')

class Horse(Pet):
    def voice(self):
        print('Horse works all the day, but she died')

    def girl(self):
        print('DADDY LOOK THAT"S A PONY')

dog = Dog('Fido', 7, 23, 54)
cat = Cat('Pussycat', 9, 8, 23)
cow = Cow('Buryonka', 4, 312, 164)
parrot = Parrot('General', 47, 3, 14)
horse = Horse('Loshadz', 5, 500, 180)

