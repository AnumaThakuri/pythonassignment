#wap to print first n fibonacci numbers upto a range given by the user:
num=int(input("Enter a range"))
a=0
b=1
c=0
while c<num:
    print (c)
    a=b
    b=c
    c=a+b 