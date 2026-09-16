list1=[]
for i in range(0,7):
    b=int(input("enter the integer"))
    list1.append(b)
min=list1[0]#cosidering the min element of the lost as 1 st one
for i in range(0,7):#comparing all elements in the list fromm minimum
    if(list1[i]<min):
        min=list1[i]
print("the smallest element in the list is",min)
max=list1[0]#considering the max elemnt of the list as the 1st one
for i in range(0,7):#comparing all the lements from the list 
    if(list1[i]>max):
        max=list1[i]
print("the largest element in list is",max)