#wap to input marks of 5 subject and find average and assign grade
sub1=int(input("Enter the marks of subject 1 :"))
sub2=int(input("Enter the marks of subject 2 :"))
sub3=int(input("Enter the marks of subject 3 :"))
sub4=int(input("Enter the marks of subject 4 :"))
sub5=int(input("Enter the marks of subject 5 :"))
sum=sub1+sub2+sub3+sub4+sub5
avg=sum/5
if(avg>90):
    print("Your grade is O")
elif(avg<=89):
    print("Your grade is E")
elif(avg<=79):
    print("Your grade is A")
else:
    print("Your garde is B")