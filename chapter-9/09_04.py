import os
os.system("cls")

# with in files in python

# this syntex automatically close file after querying it
# we dont need to write f.close() at the end
with open("sample.txt","r") as f :
    a = f.read()

with open("sample.txt","a") as f :
    a = f.write("\nAgain appended")


print(a)
