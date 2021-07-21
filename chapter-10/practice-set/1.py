import os

os.system("cls")


class Programmer:
    def __init__(self, name, skills, company):
        self.name = name
        self.skills = skills
        self.company = company

    def displayInformation(self):
        print(f"Name : {self.name}")
        print(f"Company : {self.company}")
        print(f"Skills : {self.skills}")


abdullah = Programmer("Abdullah Mehboob", ["HTML", "CSS", "ReactJs"], "Home")
tehreem = Programmer("Tehreem Mehboob", ["Sleep", "Eating", "Doing Pop"],
                     "Home")
abdullah.displayInformation()
tehreem.displayInformation()
