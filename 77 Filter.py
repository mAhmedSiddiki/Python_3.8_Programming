#filter
#filter = function,sequence

def hey(x):
    return x**2;

a = [1,2,3,4,5,6,7,8,9,10]

r = list(filter(hey,a))

print(r)

r = list(filter(lambda x:x%2 == 0,a))

print(r)