class Animal:
    def __init__(self, race, sound):
        self.race = race
        self.sound = sound

    def make_sound(self):
        print(f"{self.race} says: {self.sound}")

bird = Animal('bird', 'Piou')
dog = Animal('dog', 'bark')
cat = Animal('cat', 'Meow')

dog.make_sound()
bird.make_sound() 
cat.make_sound()



class Dog(Animal):
    def __init__ (self, name):
        super().__init__(name, "Bark!")

class Cat(Animal):
    def __init__ (self, name):
        super().__init__(name, "Meow!")

class Bird(Animal):
    def __init__ (self, name):
        super().__init__(name, "Piou!")

Dog1 = Dog('Oslo')
Cat1 = Cat('Aziza')
Bird1 = Bird('Coco')

Dog1.make_sound()