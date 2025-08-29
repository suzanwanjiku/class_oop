# Activity 2: Polymorphism Challenge 

class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def move(self):
        return "Running on the ground"

class Fish(Animal):
    def move(self):
        return "Swimming in the water"

class Bird(Animal):
    def move(self):
        return "Flying in the sky"

animals = [Dog(), Fish(), Bird()]

for animal in animals:
    print(animal.move())
