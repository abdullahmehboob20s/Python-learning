import os
os.system("cls")


# Q) Write a program to print third,fifth and seventh element from a 
#    listusing "enumerate" function

a = [1,2,3,4,5,6,7,8,9,10]

for index,num in enumerate(a) :
    if(index+1 == 3 or index+1 == 5 or index+1 == 7 ) :
        print(f"{index}) {num}")