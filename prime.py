num=int(input("enter the number of your choice"))
count=0
if(num==1):
    print("it is not a prime number")
elif(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("it is a composite number")
            break
        else:
            count=count+1
if(count!=0):
    print("it is a prime number")

else:
    print("program end")