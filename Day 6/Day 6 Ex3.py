seq= int(input("Enter no: "))
a, b= 0, 1
count= 0

while count<seq:
    print(a)

    c = a + b
  
    a= b
    b= c
    count+= 1

