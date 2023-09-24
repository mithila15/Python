#read only --> you can not set the value ,,, value can not be changed
#getter --> get a value of a property through a method,,.mosst of the time, you will get the value 
 #          of a private attribute

#setter --> set a value of a property through a method .. Most of the time, you will set the value of a private property



class User:
    def __init__(self,name,age,money) -> None:
        self.name = name
        self.age =age
        self.__money = money
    #@property
    #def age(self):
     
    #return self._age

    # getter without any setter is randomly attribute
    @property  
    def salary(self):
        return self.__money
    
    
    @salary.setter
    def salary(self,value):
        if value<0:
            return('salary can not be negative')

        self.__money += value

samsu = User('Kopa',21,12000)
#print(samsu.__money)
#print(samsu.age)
#print(samsu.salary())


samsu.salary = 450000
print(samsu.salary)