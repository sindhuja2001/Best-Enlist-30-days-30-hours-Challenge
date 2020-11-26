#Write  a Program to create a lisr of n integer values
#i)Add an item into a list

A= [1, 2, 3, 4, 5]
print(A)
A.insert(4, 6)
print(A)

#ii)Delete an item
A.remove(3)
print(A)

#iii)Store the largest number
B= max(A)
print(B)

#iv)Store the smallest number
C= min(A)
print(C)

#2) Create a tuple and print the reverse of created tuple
A= (1, 2, 3, 4, 5)
reverse= A[::-1]
print(reverse)

#3) Create a tuple and convert into list

A= (1, 2, 3, 4, 5)
print(A)
C= list(A)
print(C)