import os
os.system("cls")

# replace the multiple bad words with censor in "poem.txt"

content = ""
words = ["donkey","shut up","pagal","jahil"]

with open("poem.txt","r") as f :
    content = f.read()

for word in words :
    content = content.replace(word,"$$$$%**&%^%^$")

with open("poem.txt","w") as f2 :
    f2.write(content)