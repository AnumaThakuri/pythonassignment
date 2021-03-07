num=int(input("Enter a number"))
factorial=1
if num<0:
    print("Factorial is defined only foe positive number")
elif (num==0):
    print("Factorial for 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num ,"is",factorial)