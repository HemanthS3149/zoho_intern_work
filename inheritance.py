#Inheritance example
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
class Car(Vehicle):
    def __init__(self,make,model,year,doors):
        super().__init__(make,model,year)
        self.doors=doors

    def display_info(self):
        return f"{super().display_info()} with {self.doors} doors"

car=Car("Toyota","Corolla",2020,4)
print(car.display_info())

#Abstract class example
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow"
animals=[Dog(),Cat()]
for animal in animals:
    print(animal.make_sound())