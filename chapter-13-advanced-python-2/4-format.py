import os
os.system("cls")

# "format" same as "f" string
# Sytnx
# "str {}".format("name")

name = "Abdullah mehboob"
channel = "Abdullah-Gaming"
gender = "Male"

# a = f"This is {name}"

# or
a = "This is {}".format(name)
b = "This is {} and his channel is {}".format(name,channel)
c = "This is {1} and his channel is {2}, his gender is {0}".format(gender,name,channel)
d = "My name was, {}".format("Maaz Mehboob")


print(d)