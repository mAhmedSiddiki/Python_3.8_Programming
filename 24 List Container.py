p = ["Dog","Cat","Cow","Rat","Monkey"]

print(p)
print(len(p)) #length = 5
print(p[3],p[-2]) #length - 2 = 3
print(p[4],p[-1]) #length - 1 = 4

q = [1,2,3,4,5]

i=0
while i<len(q):
    print(q[i]," : ",p[i])
    i=i+1