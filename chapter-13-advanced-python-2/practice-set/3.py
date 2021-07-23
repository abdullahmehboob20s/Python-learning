import os
os.system("cls")

# Q) Write a program to filter a list of numbers which are divisible by 5

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,45,55,20,100,32,354,455]
fil = filter(lambda a : a%5 == 0, l)
print(list(fil))