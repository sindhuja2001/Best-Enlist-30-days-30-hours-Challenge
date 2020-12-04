#1)Write a program using zip() and list(), create a merged list of tuples from two lists given
def merge(list1, list2):
    A= tuple(zip(list1, list2))
    print(A)
list1= [1, 2, 3, 4]
list2= ['a', 'b', 'c', 'd']

print(merge(list1, list2))

#2) Using sort(), sort the list in ascending order

A= [10, 3, 5, 9]
res= A.sort()
print(A)

#3) Filter the even numbers so that only's odd numbers are passed into the new list

A= [1, 2, 3, 4, 5]
res= []

for i in A:
    if i%2!= 0:
        res.append(i)
print(res)


