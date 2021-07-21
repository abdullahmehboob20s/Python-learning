import os

os.system("cls")

a = 54  # global variable


def func1():
    global a
    a = 8  # local varible, if global keyword is not used
    print(a)


func1()
print(a)