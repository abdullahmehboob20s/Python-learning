import os

os.system("cls")

# object-oriented-programming


class RailwayForm:
    formType = "Railway Form"

    def printData(self):
        print(f"Name : {self.name}")
        print(f"Train : {self.train}")


a = RailwayForm()

a.name = "Abdullah Mehboob"
a.train = "abdullah express"
a.printData()
