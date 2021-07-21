import os

os.system("cls")

# create a class Pets from a class Animals and further create class Dog from Pets . Add a method "bark" to class Dog


class Animals:
    animalType = "Mammal"


class Pets(Animals):
    color = "white"


class Dog:
    @staticmethod
    def bark():
        print("Bow bow...")


d = Dog()
d.bark()