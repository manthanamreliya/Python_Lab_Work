X1=int(input("Enter the value of X1:"))
Y1=int(input("Enter the value of Y1:"))
X2=int(input("Enter the value of X2:"))
Y2=int(input("Enter the value of Y2:"))
X3=int(input("Enter the value of X3:"))
Y3=int(input("Enter the value of Y3:"))

slope1=(Y2-Y1)/(X2-X1)
slope2=(Y3-Y2)/(X3-X2)

if(slope1==slope2):
    print("Given points are lie on same line.")
else:
    print("Given points are not lie on same line.")
