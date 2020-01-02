#list and tuple matching

a = [1,2,9,3,9,4,9] #List
b = (7,5,7,6,7,8,7)#tuple

print("a = ",max(a)," | ","b = ",max(b))
print("a = ",min(a)," | ","b = ",min(b))
print("a = ",len(a)," | ","b = ",len(b))
print("a = ",a.index(4)," | ","b = ",b.index(7))
print("a = ",a.count(9)," | ","b = ",b.count(7))