list1=[]#defining original list 
for i in range(0,5):#input all the elemnts of the list
    c=input("enter the element of the list")
    list1.append(c)

print(list1)
list2=[]#create a new list  for copying reversed lst
for i in range(4,-1,-1):
    list2.append(list1[i])
print("the reversed list is",list2)#printing elemnts of the reversed list
