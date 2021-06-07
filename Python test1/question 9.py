#find the sum of fibonacci series up to a given range inputted by us.
n=int(input("Enter the value of n :"))
if(n<1):
    print(n)
else:
    sum=0
    a=0
    b=1
    sum=a+b
    for i in range(2,n+1):
        c=a+b
        sum=sum+c
        a=b
        b=c
    print(sum)