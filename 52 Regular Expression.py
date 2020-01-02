#regular expresion
import re #r= = regular and e = expresion

a = "My name is Rahim and i am a student"

#re.search(pattern,string,flags<optional>)
# (.*---.*)
# . means match any charecter
# * means zero or more
# flags <optional>
# re.I means case insensitive

p = re.search(".*off.*",a,re.I)

if p:
    print("Found")
else:
    print("Not Found")