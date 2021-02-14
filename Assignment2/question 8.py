sub1=float(input("Enter the marks of 1st subject : "))
sub2=float(input("Enter the marks of 2st subject : "))
sub3=float(input("Enter the marks of 3st subject : "))
sub4=float(input("Enter the marks of 4st subject : "))
sub5=float(input("Enter the marks of 5st subject : "))
total=sub1+sub2+sub3+sub4+sub5
avg=total/5
if(avg>=90):
    print("Your grade is O")
elif((avg>=80) and (avg<=89)):
    print("your garde is E")
elif((avg>=70) and (avg<=79)):
    print("Your grade is A")
else:
    print("Your grade is B")