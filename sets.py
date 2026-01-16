week=[1,4,4,5,6,6]
sets=set(week)
print (sets)

#it throws an error because we cannot access elements in sets
#print(sets[1])

#check if element exists in set
if 3 in sets:
    print("yes")
else:
    print("no")

#add element to set
sets.add(8)
sets.add(9)
print (sets)

#remove elements from set
sets.remove(9)
sets.remove(4)
print(sets)

#set opperations
a={1,2,3,4,5}
b={6,7,8,4,5}

#union
print(a.union(b))
print(a|b)

#intersection (common elements)
print(a.intersection(b))
print(a&b)

#difference (unique elements of first set)
print(a.difference(b))
print(a-b)

#symmetry difference (union-intersection)
print(a.symmetric_difference(b))
print(a^b)