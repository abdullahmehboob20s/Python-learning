import os

os.system("cls")

# else will occured when the try code do not go in "excep"

try:
    i = int(input("Enter a number : "))
    c = 1 / i

except Exception as e:
    print("Exception occured")

else:
    print("🔥 Success, Else occured")