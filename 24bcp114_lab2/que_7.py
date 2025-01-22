year=int(input("Enter the year:"))
if(year%100==0):
    if(year%400==0):
     print("Given year is leap year")
    else:
     print("Given year is not leap year")
elif(year%4==0):
    print("Given year is leap year")
else:
    print("Given year is not leap year")
