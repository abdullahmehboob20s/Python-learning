import os
os.system("cls")

# Re-naming a file

oldName = "copy.txt"
newName = "copy-of-this.txt"

with open(oldName) as f :
    content = f.read()

with open(newName,"w") as f :
    f.write(content)

os.remove(oldName)