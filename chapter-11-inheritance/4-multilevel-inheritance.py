import os

os.system("cls")

# multiLevel-inheritance


# Parent
class Person:
    country = "Pakistan"
    city = "Karachi"
    gender = "male"

    def takeBreath(self):
        print("I am breathing...")


# Child
class Employee(Person):
    company = "Youtube"
    salary = 1000000

    def getSalary(self):
        print(f"Salry is {self.salary}")

    def takeBreath(self):
        print("I am an employee so, I am breathing also")


# Grand-Child
class Programmer(Employee):
    company = "Fiver"

    def getSalary(self):
        print("No salary to programmers")

    def takeBreath(self):
        print("I am Programmer so, I dont breath")


p = Person()
e = Employee()
pr = Programmer()

print(e.company)
print(pr.company)