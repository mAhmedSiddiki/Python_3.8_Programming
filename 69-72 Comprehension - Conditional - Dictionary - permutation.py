#list comprehension

a = [x for x in range(1,500)]

print(a)

#comprehension and conditional

a = [x for x in range(1,11) if x%2 == 0]
#expresion, range/enumerate = f(x) = x^2,condition

print(a)

a = [x**2 for x in range(1,11) if x%2 == 0]
print(a)

#comprehension - dictionary
a = {x**2:x for x in range(1,10)}
print("Dictionary: ",a)


#comprehension - permutation
#(a,b)(a,b) = {(a,a),(a,b),(b,a),(b,b)}

a = ["a","b"]
b = [2,3]

s = [(x,y) for x in a for y in b]

print("Permutation: ",s)