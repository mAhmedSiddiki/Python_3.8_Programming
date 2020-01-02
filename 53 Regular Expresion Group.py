#regular expresion
import re #r= = regular and e = expresion

a = "My name is Rahim and i am a student"

#re.search(pattern,string,flags<optional>)
# (.*---.*)
# . means match any charecter
# * means zero or more
# flags <optional>
# re.I means case insensitive

p = re.search("(.*)and(.*)",a,re.I)

if p:
    print("Found")
    print(p.group())
    print(p.group(1))
    print(p.group(2).upper())
else:
    print("Not Found")