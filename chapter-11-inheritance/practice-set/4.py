import os

os.system("cls")


class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def add(self, c):
        return Complex(self.real + c.real, self.imaginary, c.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


c1 = Complex(1, 4)
c2 = Complex(8, 5)

print(c1 + c2)
