#wap to print prime number between 98 and 1004:
print("Prime numbers between 30 and 100")
for num in range(98,104+1):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num)