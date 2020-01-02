#list and tuple compare

a = [1,2,3] #list
b = (4,5,6) #tuple

a.append(10)
#b.append(10)

c = tuple(a)
#c.append(10)

d = list(b)
d.append(10)

print("a = ",a)
print("b = ",b)
print("c = ",c)
print("d = ",d)

b = tuple(d)
print("b = ",b)