num1=int(input("enter 1st number :"))
num2=int(input("enter 2nd number :"))
num3=int(input("enter 3rd number :"))
if((num2>num1 and num1>num3) or (num3>num1 and num1>num2)):
    print(num1,"is second samllest number")
elif((num1>num2 and num2>num3) or (num3>num2 and num2>num1)):
    print(num2,"is second smallest number")
elif((num1>num3 and num3>num2) or (num2>num3 and num3>num1)):
    print(num3,"is the second smallest number")


