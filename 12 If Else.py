a = 5
b = 8

if a < b:
    print("a is small")
else:
    print("b is small")


c = int(input("Enter a first number: "))
d = int(input("Enter a second number: "))

if c < d:
    print("first number is small")
    print("second number is big")
elif c==d:
    print("first and second number is equal")
else:
    print("first number is big")
    print("second number is small")