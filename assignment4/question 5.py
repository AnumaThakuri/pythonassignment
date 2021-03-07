n=int(input("Enter a integer"))
x=n
y=0
while(n>0):
    r=n%10
    y=(y*10)+r
    n=n//10
if(x==y):
    print("The number is palindrome")
else:
    print("The number is not a palindrome")