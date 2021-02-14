sub1=float(input("Enter the marks of subject 1 :"))
sub2=float(input("Enter the marks of subject 2 :"))
sub3=float(input("Enter the marks of subject 3 :"))
sub4=float(input("Enter the marks of subject 4 :"))
total=sub1+sub2+sub3+sub4
avg=total/4
print("Your average marks =",avg)
if(avg<=40):
    print("Sorry you are failed")
elif(avg>40):
    print("Congratulations you are passed")