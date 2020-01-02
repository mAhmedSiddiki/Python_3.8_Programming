#searching - gmail
import re

a = input("Enter your email: ")

#re.search(pattern,string,flags<optional>)
#\w = word charecter
#+ = one or more
#* = zero or more
#. = any charecter

p = re.search("\w+\.*\w+@\w+\.\w+",a)

if p:
    print("Found")
else:
    print("Not Found")