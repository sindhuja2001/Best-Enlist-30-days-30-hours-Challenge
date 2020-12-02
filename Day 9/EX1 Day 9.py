#1) Create a lambda function that multiplies argument x with argument y

def multiply(n):
    return lambda x: x*n
res= multiply(10)
print(res(5))

#3)Multiply each number of given list with a given number

A= [1, 2, 3, 4, 5]
n=2
print(A)
print(n)
B= list(map(lambda num: num*n, A))
print(' '.join(map(str, B)))

#4) To find numbers divisible by 9 from a list of numbers
A= [1, 9, 2, 18, 4]
res= list(filter(lambda x: (x%9== 0), A))
print(res)

#5) To find the even numbers in the list
A= [1, 2, 3, 4, 5]
res= list(filter(lambda x: (x%2== 0), A))
print(res)
