import os

os.system("cls")

print("Press q to exit")

while True:
    a = input("Enter a number  : ")

    if a == "q":
        break

    try:
        a = int(a)
        if a > 6:
            print("You entered a number greater than 6")

    except Exception as e:
        print("\nInvalid input! 😔\n")

print("Thanks for playing this game")