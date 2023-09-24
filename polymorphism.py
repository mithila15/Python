# poly ---> many
#morph --> differet shape 

class Animal:
    def __init__(self,name ) -> None:
        self.name = name

    def make_sound(self):
        print('animal making sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('meaw meaw')


class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('Ghewww gheeeww')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Yes we won the World cup!')



don = Cat ('Rea don')
don.make_sound()

shepahred = Dog('Local shephered')
shepahred.make_sound()

mess = Goat ('L M')
mess.make_sound()

less = Goat('gora gori')


animals = [don,shepahred,mess,less]
for animal in animals:
    animal.make_sound()