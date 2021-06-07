#wap that reads two number and an arithmetic operator and displays the result:
num1=float(input("Enter the 1st number : "))
num2=float(input("Enter the 2st number : "))
op=input("Enter the operator : ")
result=0
if(op=="+"):
    print("Result",num1+num2)
elif(op=="-"):
    print("Result",num1-num2)
elif(op=="*"):
    print("Result",num1*num2)
elif(op=="/"):
    print("Result",num1/num2)