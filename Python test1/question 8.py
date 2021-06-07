'''print the following
a
b c
d e f 
g h i j'''

n=int(input("Enter the number of rows :"))
k=ord("a")
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()