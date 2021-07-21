import os
os.system("cls")

f = open("sample.txt","r") 
data = f.readline()
print(data)
f.close()