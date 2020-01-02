#regular expresion wprd substitution
import re
a = "this is a number 1234 5678"

#re.sub(pattern,replacement,string)
#\w = word charecter

p = re.sub("\w+","$",a)

print(p)

p = re.sub("\w+s","$",a)

print(p)

p = re.sub("\d","$",a)

print(p)

p = re.sub("\D","$",a)

print(p)