#print the prime number between 100 and 30
print("Prime numbers between 30 and 100")
for num in range(30,100+1):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        print(num)