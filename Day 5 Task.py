#1)Create a function getting 2 integers input from user
#i)Add, Subtract, Multiply, divide two integers


def add2NUm(a, b):
     sum= a+b
     diff = a - b
     multiply = a * b
     divide = a / b
     return sum, diff, multiply, divide

a= int(input("Enter the first value: "))
b= int(input("Enter the second value: "))

print(add2NUm(a, b))

# 2) Create and function and enter the following:
# i) Patient name and temperature

def covid(name, temp= 98):
    print("Patient name", name, "temp is: ", temp)

covid("A", 98)
covid("B", 100)





