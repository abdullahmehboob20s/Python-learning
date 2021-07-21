import os

os.system("cls")

# Q) can we rename "self" parameter in class ?


class Student:
    def __init__(mySelf, name):
        mySelf.name = name


a = Student("Abdullah Mehboob")
print(a.name)