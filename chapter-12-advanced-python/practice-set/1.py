import os
os.system("cls")

# Q) Write a program to open three files (1.txt , 2.txt , 3.txt)
#   If any of these files are not present, a message without  
#   exiting the program must be printed, prompting the same 

def readFile(filename) :
    try:
        with open(filename,"r") as f:
            print(f.read())
            
    except FileNotFoundError : 
        print(f'File "{filename}" is not found')

readFile("4.txt")