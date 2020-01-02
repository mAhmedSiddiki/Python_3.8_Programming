#reduce

from functools import reduce

def func(x,y):
    return x*y

a = [1,2,3,4,5]
b = reduce(func,a)
print(b)

b = reduce(lambda x,y:x*y,a)
print(b)