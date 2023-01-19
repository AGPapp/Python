#Необходимо дополнить "Практическое задание №6" таким образом, чтобы в конце программы мы вызвали статический метод родительского
#класса Animal, который вывел бы нам количество всех созданных экземпляров.
#Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3.

class Animal:
    kolvo = 0

    def __init__(self): Animal.kolvo = Animal.kolvo + 1

    def voice(self):
        pass


class Maus(Animal):
    def voice(self):
        return "pi-pi-pi-pi"


class Cat(Animal):
    def voice(self):
        return "mr-mr-mr-mr"


class AngryCamel(Animal):

    def voice(self):
        return "aa-pp-tfff-uuu"


mikkiMaus = Maus()
kitty = Cat()
vasia = AngryCamel()

print(mikkiMaus.voice())
print(kitty.voice())
print(vasia.voice())

def print_kolvo(): print('\n', Animal.kolvo)
print_kolvo()