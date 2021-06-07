#print all three digits Armstrong number.
for n in range(100,1000):
    temp=n
    sum=0
    while temp>0:
        a=temp%10
        sum+=a**3
        temp//=10
    if n==sum:
        print(n)