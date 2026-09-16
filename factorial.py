num=int(input("enter number of your choice"))
fact=1
if(num==0):
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i

print("factorial of{}is{}".format(num,fact))