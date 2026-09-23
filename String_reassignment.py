def change_string(s):
    list1=list(s)
    list1[0]='X'
    s="".join(list1)
    return s
given_string=""
given_string=input("enter the string to be used for operation reassignment")
print(given_string)
changed_string=change_string(given_string)
print(changed_string)
print(given_string)
if(changed_string==given_string):
    print("the string changes both inside and out of the function")


