#Design a Simple Calculator with try and except for all use cases
def add():
    try:
        res= a+b
        print(res)
    except Exception as e:
        print(e)
def subtract():
    try:
        res= a-b
        print(res)
    except Exception as e:
        print(e)
def multiply():
    try:
        res= a*b
        print(res)
    except Exception as e:
        print(e)
def divide():
    try:
        res= a/b
        print(res)
    except Exception as e:
        print(e)
try:
    a= int(input("Enter a num: "))
    b= int(input("Enter a num: "))
    add()
    subtract()
    multiply()
    divide()
except Exception as e:
    print("You can enter only integers")