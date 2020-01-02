mark = int(input("Enter your subject number out of 100: "))

if mark>=80:
    if mark <= 100:
        print("A+")
elif mark>=75:
    if mark<=79:
        print("A")
elif mark>=70:
    if mark<=74:
        print("A-")
elif mark>=65:
    if mark<=69:
        print("B+")
elif mark>=60:
    if mark<=64:
        print("B")
elif mark>=55:
    if mark<=59:
        print("B-")
elif mark>=50:
    if mark<=54:
        print("C+")
elif mark>=45:
    if mark<=49:
        print("C")
elif mark>=40:
    if mark<=44:
        print("D")
elif mark>=0:
    if mark<=39:
        print("F")
