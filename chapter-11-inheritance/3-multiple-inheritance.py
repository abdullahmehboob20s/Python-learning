import os

os.system("cls")

# multiple-inheritance

# multiple inheritance occurs when the child class inherits from more than one parent class


class Parent1:
    name = "Parent-1"
    key = "Parent-1: I have car"
    gender = "male"


class Parent2:
    name = "Parent-2"
    gender = "female"
    msg = "Parent-2: I am the owner of house"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Child(Parent1, Parent2):
    name = "child"
    disc = "child: I am a child"


c = Child()
print(c.gender)