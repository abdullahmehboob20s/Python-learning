import os
os.system("cls")

a = open("poem.txt","r")
b = a.read()
print("twinkle" in b)
a.close()