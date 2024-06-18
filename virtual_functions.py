#Base class for animal
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #Abstract method for sound 
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement make_sound method")
    
    def move(self):
        raise NotImplementedError("Subclasses must implement move method")
    
    def feed(self):
        raise NotImplementedError("Subclasses must implement feed method")
    
    def display_info(self):
        print(f"{self.__class__.__name__}: {self.name},Age: {self.age}")
        
#Subclasses
class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} the Lion roars!")
    
    def move(self):
        print(f"{self.name} the Lion is being fed with meat.")

    def feed(self):
        print(f"{self.name} the lion is being fed with meat")

#elephant
class Elephant(Animal):
    def make_sound(self):
        print(f"{self.name} the Elephent trumpets!")

    def move(self):
        print(f"{self.name} the Elephant slowly walks around")

    def feed(self):
        print(f"{self.name} the Elephant is being fed food")

lion=Lion("Simba",5)
ele=Elephant("Dumbo",10)

lion.display_info()
ele.display_info()

print("\nPerforming actions:")
lion.feed()
lion.make_sound()
lion.move()

ele.feed()
ele.make_sound()
ele.move()