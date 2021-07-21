import os

os.system("cls")


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def getDetails(self):
        print(self.name)
        print(self.grade)


a = Student("Abdullah Mehboob", "1st Year")
a.getDetails()