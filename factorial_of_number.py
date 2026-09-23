def factorial(num):
    fact=1;
    for i in range(num,0,-1):
     
        fact=fact*i
    return fact
number=int(input("enter the number to be found factorial of"))
factorial(number)
print("the factoraial of number",number," is",factorial(number))