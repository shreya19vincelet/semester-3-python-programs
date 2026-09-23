def remove_last(lst):
    lst.remove(lst[4])
    print(lst)
    return lst
list1=[]
for i in range(5):
    c=int(input("enter the element"))
    list1.append(c)
print(list1)
mutated_list=remove_last(list1)
print(list1)
if(mutated_list==list1):
    print("the list changes for both inside and out of the function")
    
