import os
os.system("cls")

# Write a program to display the value of a/b where "a" and "b" are integers. If b=0, display infinite by handling the "ZeroDivisionError"  


a = 12
b = 0

try : 
    print(a/b)

except ZeroDivisionError as a :
    print(f"{a}, Infinite value")