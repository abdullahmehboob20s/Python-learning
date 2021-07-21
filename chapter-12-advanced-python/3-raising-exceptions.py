import os

os.system("cls")


def increament(num):
    try:
        return int(num) + 1

    except:
        raise ValueError("This in not good")
        # print("This is not good")


print(increament(32))