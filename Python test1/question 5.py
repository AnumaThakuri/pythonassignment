#print fibonacci series <100. and also print reverse fibonacci series:
n=int(input("Enter the value of n :"))
a=0
b=1
c=0
print("Fibonacci series :")
while c<n:
    print(c)
    a=b
    b=c
    c=a+b
