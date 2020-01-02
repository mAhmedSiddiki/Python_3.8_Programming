#word reverse

a = "i love you"

b = a.split()
c = b[::-1]
d = " ".join(c)

print(b)
print(c)
print(d)

print(" ".join(a.split()[::-1]))