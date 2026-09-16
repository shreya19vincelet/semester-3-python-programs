fruits=[]#defining a lst in the program to use
print("input a list of your choice having name of 5 fruits")#input the lost from the user 
for i in range(0,5):
    b=input("enter the fruit name")
    fruits.append(b)
#printing the list containing fruits name
for i in range(0,5):
    print(fruits[i])

print(fruits[1])#2 nd item is present at the 1 st index
print(fruits[3])# 4 th item is present at the 3 rd index of the list
fruits[4]="mango"#update the last element of te list fruits as mango
print(fruits)#printing the updated list 