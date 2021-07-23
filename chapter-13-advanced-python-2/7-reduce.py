import os
from functools import reduce
os.system("cls") 

# reduce
# we have to import "reduce" first to use it


add = lambda a,b : a+b

l = [1,2,3,4]
val = reduce(add,l)
print(val)