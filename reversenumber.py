num=int(input("enter the number of your choice"))
num2=num
sum=0
while(num2!=0):
    t=num2%10
    sum=sum*10+t
    num2=num2//10
print(sum)