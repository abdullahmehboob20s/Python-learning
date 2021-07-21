import os
import random

os.system("cls")

randomNumber = random.randint(1, 100)
guessed = False
guesses = 0

while guessed != True:
    userGuess = int(input("Guess any number between 1-100: "))

    if (userGuess == randomNumber):
        print(f"\n😀 You Guessed it right! in {guesses} rounds")
        guessed = True
        with open("The-perfect-guess/score.txt", "w") as f:
            f.write(f"result = {userGuess}\nYou guessed in {guesses} rounds")

    elif (userGuess > 100 or userGuess <= 0):
        print("Please enter value between 1 to 100")
        guesses = guesses + 1

    elif (userGuess > randomNumber):
        print("Your guess is higher")
        guesses = guesses + 1

    elif (userGuess < randomNumber):
        print("Your guess is lower")
        guesses = guesses + 1

    else:
        print("Invalid Input! 😔")
