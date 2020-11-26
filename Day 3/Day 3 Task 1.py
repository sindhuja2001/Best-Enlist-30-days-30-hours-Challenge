#To merge two python Dict

A= {1: "C", 2: "Python", 3: "C++"}
B= {4: "AWS", 5: "Cloud", 6: "Database"}
merge=  A.copy()
merge.update(B)
print(merge)


# Remove a key from a dictionary

A= {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(A)
if 'a' in A:
    del A['a']
print(A)

#To map two lists in Dictionary

A= {1, 2, 3, 4}
B= {'C', 'C++', 'Python'}
map= dict(zip(A, B))
print(map)

#To find the length of a set

setA= set([1, 2, 3, 4, 5])
print(len(setA))


#To remove the intersection of 2nd set into 1st set

A= set([1, 2, 3, 4, 5])
B= set([3, 4, 5, 6, 7])
print(A)
print(B)
A.difference_update(B)
print(A)

