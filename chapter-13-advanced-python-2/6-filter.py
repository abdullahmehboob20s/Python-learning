import os
os.system("cls")

# filter


# return "True" if greater than 5
def greater_than_5(num) :
    if num>5:
        return True
    else :
        return False

# return "True" if greater than 10
greater_than_10 = lambda num : num > 10

l = [2,3,4,5,6,43,331]

# Method without "filter"
l2 = []
for i in l :
    if greater_than_5(i) :
        l2.append(i)
print(l2)

# Method with "filter"
print(list(filter(greater_than_5, l)))
print(list(filter(greater_than_10, l)))
