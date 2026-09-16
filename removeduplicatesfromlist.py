list1=[]#definning list 1
list2=[]#defining the list 2
num=int(input("enter the number  of elements to be entred in the list"))
for i in range(0,num):#input all elements in the list 1
    c=input("enter the integer")
    list1.append(c)
for i in range(0,num):#appending all the non repetetive elements in lst 2
    if(list1[i] not in list2):
        list2.append(list1[i])
print("the updated list is")
print(list2)