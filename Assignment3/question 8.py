def prime_number(n):
    f=0
    if n>1:
        for i in range(2,n):
            if n%i==0:
                f=1
                break
    else:print("invalid input")
return f
num=int(input("Enter number to check prime"))
result=prime_number(num)
if result==0
   print("number is prime")
else:
    print("number is not prime")