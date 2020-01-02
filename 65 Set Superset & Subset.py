#superset and subset

set1 = {1,2,3,4,5,6,7}
set2 = {3,4,5}

# > = superset
# < = subset

print(set1 > set2)
print(set1 < set2)

print(set1.issubset(set2))
print(set1.issuperset(set2))