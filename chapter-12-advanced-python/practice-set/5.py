import os
os.system(("cls"))

# Q) write a list comprehension to print in a file which contains the
#    multiplication table of a user entered number.

num = 54
table = [num*i for i in range(1,11)]

with open("table.txt","a") as f :
    f.write(f"Table of {num} = {table}")
    f.write("\n")