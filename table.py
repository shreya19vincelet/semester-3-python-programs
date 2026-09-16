num=int(input("enter the number to be printed table of "))
print("the table of the number{}is:".format(num))
for i in range(1,11):
    print("{}*{}={}".format(num,i,(num*i)))
print("table printed")