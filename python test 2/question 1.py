''''print thr following:
0
1 0
0 1 0
1 0 1 0'''
n=int(input("Enter the number of rows :"))
count=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(count%2,end=" ")
        count+=1
    print()
    if (i%2==1):
        count=1
    else:
        count=0