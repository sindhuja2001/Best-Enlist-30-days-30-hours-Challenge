A= [1, 2, 3, 4, 5]
B= 2
res= [x + B for x in A]
print(res)

#5) Table of 9

num= 9
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

#6) Program is positive or negative

num= int(input("Enter a number: "))
if num>0:
    print("Num is positive", num)
elif(num== 0):
    print("Zero")
else:
    print("Negative")

#7) No od days to years

num= int(input("Enter no of Days: "))
years= num/365
print(int(years))


