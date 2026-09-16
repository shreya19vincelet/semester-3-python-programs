numbers=[]#defining list in the program
for i in range(0,10):#input the list via user
    c=input("enter the number")
    numbers.append(c)    #append the lost one by one with the numbers
for j in range(0,10):   #printing the input list
    print(numbers[j])
sum=0
for k in range(0,10):#sum of the elements of the given list
    sum=sum+int(numbers[k])
print("the sum of all the elemennts of the list is ",sum)
average=0
average=(sum)/10 #finding the average of the given elements in the list by using the pre existing sum of the elements of the list
print("average of the numbers are as follows",average)
