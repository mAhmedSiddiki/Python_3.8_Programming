#map

def hey(x):
    return x**2

b = [1,2,3,4,5]

a = list(map(hey,b))
c = list(map(lambda x:x**2,b))

print(a)
print(c)