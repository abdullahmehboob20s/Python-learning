import os
os.system("cls")

a = [2,1,3,12,32,39,12,100,23,0,43,300,66,89]


# Longcut ====
# b = []
# for index,item in enumerate(a) :
#     if(item%2 == 0) :
#         b.append(item)
# print(b)


# Shortcut ====
b = [num for num in a if num%2 == 0 ]
print(b)