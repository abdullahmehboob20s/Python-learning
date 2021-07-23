import os
os.system("cls")


def square(num) :
    return num*num

a = [3,2,4]

# Method 1
def method1(arr) :
    l2 = []
    for num in arr :
        l2.append(square(num))
    print(l2)


# Method 2
print(list(map(square, a)))