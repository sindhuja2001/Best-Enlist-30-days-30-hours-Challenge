num= int(input("Enter a num: "))
sum= 0
temp= num
while temp>0:
    digit= temp%10
    sum= sum+ digit**3
    temp//= 10
if(num== sum):
    print("Armstrong number: ", num)
else:
    print("Not a Armstrong number")