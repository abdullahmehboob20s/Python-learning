import os

os.system("cls")

# Q) Write a class capable of finding square,cube and square root of a number


class Calculator:
    def __init__(self, num1):
        self.number = num1

    @staticmethod
    def greet():
        print("Aslam-o-alikum, Welcome Sir!")

    def square(self):
        print(f"Square of {self.number} is = {self.number * self.number}")

    def cube(self):
        print(f"Cube of {self.number} is = {self.number**3}")

    def squareRoot(self):
        print(f"Square Root of {self.number} is = {self.number**(1/2)}")


a = Calculator(9)
a.greet()
