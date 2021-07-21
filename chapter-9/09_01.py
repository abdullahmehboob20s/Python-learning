import os
os.system("cls")

f = open("sample.txt","r") 
data = f.read()
print(data)
f.close()