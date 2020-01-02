#regular expresion - match
import re

a = "My name is Rahim and i am a student"

#re.match(pattern,string,flags<optional>)

p = re.match("(My.*)(and)(.*student)", a, re.I)

if p:
    print("Match")
    print(p.group(1))
    print(p.group(2))
    print(p.group(3))
else:
    print("Not Match")