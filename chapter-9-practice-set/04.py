import os
os.system("cls")

# replace bad words with censor in "poem.txt"

content = ""

with open("poem.txt","r") as f :
    content = f.read()

content = content.replace("shut up","$$$$%**&%^%^$")

with open("poem.txt","w") as f2 :
    f2.write(content)