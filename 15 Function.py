#function
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

print("Summation: ",sum(a,b))
print("Subtraction: ",sub(a,b))