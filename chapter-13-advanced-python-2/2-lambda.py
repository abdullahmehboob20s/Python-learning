import os
os.system("cls")

# Second way of writing functions with "Lambda"
# to define a function in one line

# Method 1
# def func(a):
#     return a+5

# Method 2
func = lambda a : a+5
square = lambda x : x*x
add = lambda a,b,c : a+b+c

print(func(100))
print(square(3))
print(add(2,2,2)) 