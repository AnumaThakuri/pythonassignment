def perfectnum(num):
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum=sum+i
    return sum==num
num=int(input("Enter a natural number :"))
if perfectnum(num):
    print("This is a perfect number")
else:
    print("This is not a perfect number")