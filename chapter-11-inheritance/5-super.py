import os

os.system("cls")

# multiLevel-inheritance


# Parent
class Person:
    country = "Pakistan"
    city = "Karachi"
    gender = "male"

    def __init__(self):
        print("Intializing Person...\n")

    def takeBreath(self):
        print("I am breathing...")


# Child
class Employee(Person):
    company = "Youtube"
    salary = 1000000

    def __init__(self):
        super().__init__()
        print("Intializing Employee...\n")

    def getSalary(self):
        print(f"Salry is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an employee so, I am breathing also")


# Grand-Child
class Programmer(Employee):
    company = "Fiver"

    def __init__(self):
        super().__init__()
        print("Intializing Programmer...\n")

    @staticmethod
    def getSalary():
        print("No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am Programmer so, I don't breath")


# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()
