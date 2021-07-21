import os
os.system("cls")

# if your score is higher than the score in "hiscore.txt" than it will overwrite the previous value

def game() :
    return 12

score = game()
with open("hiscore.txt","r") as f :
    hiscoreStr = f.read()

if hiscoreStr == ""  :
     with open("hiscore.txt","w") as f:
        f.write(str(score))

elif int(hiscoreStr) < score   :
    with open("hiscore.txt","w") as f:
        f.write(str(score))