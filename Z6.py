class Animal:
    def voice(self): pass


class Maus(Animal):
    def voice(self): return "pi-pi-pi-pi"


class Cat(Animal):
    def voice(self): return "mr-mr-mr-mr"


class AngryCamel(Animal):

    def voice(self): return "aa-pp-tfffuuu"


mikkiMaus = Maus()
kitty = Cat()
vasia = AngryCamel()

print(mikkiMaus.voice())
print(kitty.voice())
print(vasia.voice())
