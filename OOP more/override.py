class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.nmae=name 
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('I love biriyani ')

class Cricketer(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        print('vegetables')
    
    def exercise(self):
        print('go to gym!')

    def __add__(self,other):
        return self.age +other.age
     
    def __mul__(self,other):
        return self.weight * other.weight
    def __len__(self):
        return self.height
    def __gt__(self,other):
        return self.age > other.age


shakib = Cricketer('Shakib', 35,68,92,'BD')
mushi = Cricketer('mushi',36,50,80,'BD')
#shakib.eat()
#shakib.exercise()

#plus sign overload
#print(45+90)
#print('sakib'+'al'+'hasan')
#print([12,34,]+[5,6,7,1])
print(shakib + mushi)
print(shakib * mushi)
print(len(shakib))
print(shakib>mushi)