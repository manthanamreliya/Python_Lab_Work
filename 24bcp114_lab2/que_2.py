a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if(a>b):
    if(a>c):
        print("Largest:",a)
    else:
        print("Largest:",c)
else:
    if(b>c):
        print("Largest:",b)
    else:
        print("Largest:",c)
if(a>b):
    if(b>c):
        print("Smallest:",c)
    else:
        print("Smallest:",b)
else:
    if(a>c):
        print("Smallest:",c)
    else:
        print("Smallest:",a)

