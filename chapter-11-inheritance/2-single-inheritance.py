import os

os.system("cls")

# Single-inheritance


# Employee
class Employee:
    name = "abdullah"
    skills = ["HTML", "Css"]
    company = "Google"

    def showDetails(self):
        print("This is a Employee")


# Programmer
class Programmer(Employee):
    langauage = "Python"
    company = "Microsoft"

    def getLang(self):
        print(self.langauage)

    def showDetails(self):
        print("This is a Programmer")


e = Employee()
p = Programmer()

print(e.company)
print(p.company)