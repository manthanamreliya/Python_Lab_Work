sub1=int(input("Enter the marks of first subject:"))

if(sub1<=39):
    print("sub1->Fail")
    print("sub1->Grade:F")
elif(sub1<=44 & sub1>=40):
    print("sub1->Pass")
    print("sub1->Grade:P")
elif(sub1<=49 & sub1>=45):
    print("sub1->Pass")
    print("sub1->Grade:C")
elif(sub1<=54& sub1>=50):
    print("sub1->Pass")
    print("sub1->Grade:B")
elif(sub1<=59 & sub1>=55):
    print("sub1->Pass")
    print("sub1->Grade:B+")
elif(sub1<=60 & sub1>=69):
    print("sub1->Pass")
    print("sub1->Grade:A")
elif(sub1<=79 & sub1>=70):
    print("sub1->Pass")
    print("sub1->Grade:A+")
elif(sub1<=100 & sub1>=80):
    print("sub1->Pass")
    print("sub1->Grade:O")
else:
    print("sub1->Absent")
    print("sub1->Grade:NA")
    
sub2=int(input("Enter the marks of second subject:"))

if(sub2<=39):
    print("sub2->Fail")
    print("sub2->Grade:F")
elif(sub1<=44 & sub1>=40):
    print("sub2->Pass")
    print("sub2->Grade:P")
elif(sub1<=49 & sub1>=45):
    print("sub2->Pass")
    print("sub2->Grade:C")
elif(sub1<=54& sub1>=50):
    print("sub2->Pass")
    print("sub2->Grade:B")
elif(sub1<=59 & sub1>=55):
    print("sub2->Pass")
    print("sub2->Grade:B+")
elif(sub1<=60 & sub1>=69):
    print("sub2->Pass")
    print("sub2->Grade:A")
elif(sub1<=79 & sub1>=70):
    print("sub2->Pass")
    print("sub2->Grade:A+")
elif(sub1<=100 & sub1>=80):
    print("sub2->Pass")
    print("sub2->Grade:O")
else:
    print("sub2->Absent")
    print("sub2->Grade:NA")
    
sub3=int(input("Enter the marks of third subject:"))

if(sub3<=39):
    print("sub3->Fail")
    print("sub3->Grade:F")
elif(sub1<=44 & sub1>=40):
    print("sub3->Pass")
    print("sub3->Grade:P")
elif(sub1<=49 & sub1>=45):
    print("sub3->Pass")
    print("sub3->Grade:C")
elif(sub1<=54& sub1>=50):
    print("sub3->Pass")
    print("sub3->Grade:B")
elif(sub1<=59 & sub1>=55):
    print("sub3->Pass")
    print("sub3->Grade:B+")
elif(sub1<=60 & sub1>=69):
    print("sub3->Pass")
    print("sub3->Grade:A")
elif(sub1<=79 & sub1>=70):
    print("sub3->Pass")
    print("sub3->Grade:A+")
elif(sub1<=100 & sub1>=80):
    print("sub3->Pass")
    print("sub3->Grade:O")
else:
    print("sub3->Absent")
    print("sub3->Grade:NA")


print("Total:",sub1+sub2+sub3)
print("Avarage:",(sub1+sub2+sub3)/3)




