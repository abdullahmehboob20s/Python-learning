import os
import random
os.system("cls")

def gameWin(comp,you) :
    if comp == you :
        return None
    if(comp == "s" and you == "w"):
        return False
    if(comp == "s" and you == "g"):
        return True
    if(comp == "w" and you == "s"):
        return True
    if(comp == "w" and you == "g"):
        return False
    if(comp == "g" and you == "s"):
        return False
    if(comp == "g" and you == "w"):
        return True


print("Comp Turn: Snake(s) , water(w) or gun(g) ? ")
randNo = random.randint(1,3)

if randNo == 1 :
    comp = "s"
elif randNo == 2 :
    comp = "w"
else :
    comp = "g"

b = input("Your Turn: Snake(s) , water(w) or gun(g) ? ")

result = gameWin(comp,b)

if result == None :
    print(f"\nComp = {comp} , You = {b}")
    print("The game is tie!")
elif result == True :
    print(f"\nComp = {comp} , You = {b}")
    print("You Won the game!")
elif result == False :
    print(f"\nComp = {comp} , You = {b}")
    print("You Lost the game!")