l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
area=l*b
perimeter=2*(l+b)
if(area>perimeter):
    print("area of the rectangle is greater than its perimeter.")
else:
    print("area of the rectangle is not greater than its perimeter.")
