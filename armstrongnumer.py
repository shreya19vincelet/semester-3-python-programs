num=int(input("enter a number"))
count=0
sum=0
num2=num
while(num2!=0):
    t=num2%10
    count=count+1
    num2=num2//10
print("the number of digits are",count)
num3=num
while(num3!=0):
    g=num3%10
    sum=sum+(g**count)
    num3=num3//10
if(sum==num):
    print("armstrong number")
else:
    print("not an armstroong number")