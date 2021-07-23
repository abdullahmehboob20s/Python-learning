import os
os.system("cls")


# Q) Write a program to input name,marks and phone number of a student and format it using the format function like below
# "The name of the student is Harry, his marks are 72 and phone number is 89279123234"

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
number = int(input("Enter your phone number: "))

sentence = "The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,number)

print("\n"+"-"*len(sentence))
print(sentence)