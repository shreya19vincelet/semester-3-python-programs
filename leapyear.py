year=int(input("enter the year of your choice"))
if((year%400==0) and (year%100==0)):
    print("the {} year is a leap year".format(year))
elif((year%4==0)and (year%100 !=0)):
    print("the {} year is a leap year".format(year))
else:
    print("the{} year is not a leap year".format(year))