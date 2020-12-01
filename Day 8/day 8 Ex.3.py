#Print one message if it raises an error

A= input()
prit(A)

try:
    a= 1/0
except Exception as e:
    print(e)