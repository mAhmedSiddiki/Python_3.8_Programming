a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if a>b:
    if a>c:
        print("1st number is greatest")
    else:
        print("3rd number is greatest")
elif b>c:
    if b>a:
        print("2nd number is greatest")
    else:
        print("1st number is greatest")
else:
    print("3rd number is greatest")