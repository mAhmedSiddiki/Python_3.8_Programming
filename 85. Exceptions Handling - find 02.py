#Exceptions Handling - find


'''
try:
    a = int(input("Enter a number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Divided by zero")
    #another code


try:
    #a = int(input("Enter a number: "))
    print(10 / a)
except NameError:
    print("Name error")
    #another code


try:
    #a = int(input("Enter a number: "))
    print(10 / "3")
except TypeError:
    print("Type error")
    #another code
'''

try:
    a = int(input("Enter a number: "))
    print(10/a)
    print(10/b)
    print(10/'2')
except (ZeroDivisionError,NameError,TypeError):
    print("Invalid your code")