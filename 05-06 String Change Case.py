a = 'this is a string'
b = 'This Is A StRIng'

print("Capitalize: ",a.capitalize())
print("Upper Case: ",a.upper())
print("Lower Case: ",b.lower())
print("Title: ",a.title())

c = "this is a string"
print("is lower ? ",c.islower())

c = "this Is a string"
print("is lower ? ",c.islower())

d = "Marjuk"
print("is alphabetic ? ",d.isalpha())

d = "2734"
print("is alphabetic ? ",d.isalpha())

e = "Marjuk007"
print("is alphabetic and number ? ",e.isalnum())

e = "#$%^&*("
print("is alphabetic and number ? ",e.isalnum())

f = "8743248908"
print("is number ? ",f.isdigit())

f = "coding laugh"
print("is number ? ",f.isdigit())
