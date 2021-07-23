import os
os.system("cls")

# Q) A list contains the multiplication table of 7. Write a program to convert it to a vertical string of same numbers
# example
# 7 
# 14
# 21
# 28
# 35
# 42
# 49
# 56
# 63
# 70

l = [str(i*7) for i in range(1,11)]
output = "\n".join(l)
print(output)