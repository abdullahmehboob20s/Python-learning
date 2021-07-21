import os

os.system("cls")

# finaly occures when try or except code is completed
# even if we run "exit()" in try or except

try:
    i = int(input("Enter a number : "))
    c = 1 / i

except Exception as e:
    print("Exception occured")
    exit()

finally:
    print('Done, "finally" occured')