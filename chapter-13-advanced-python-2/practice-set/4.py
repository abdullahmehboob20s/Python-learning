import os
from functools import reduce
os.system("cls")

# Q) Write a program to find the maximum of the numbers in a list using the reduce function

# max(12,32) : answer = 32

l = [1,2,3,4,5,6,7,131,8,9,10,435]
print(reduce(max, l))