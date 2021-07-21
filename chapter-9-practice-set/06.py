import os
os.system("cls")

# make a copy of "this.txt" file

with open("this.txt") as f:
    content = f.read()

with open("copy.txt","w") as f2 :
    f2.write(content)