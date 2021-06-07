#take the input from the console and create 2D list:
rows=int(input("Enter the number of rows :"))
cols=int(input("Enter the numbers of columns :"))
matrix=[]
for i in range(0,cols):
    matrix.append([])
for i in range(0,rows):
    for j in range(0,cols):
        matrix[i].append(j)
        matrix[i][j]=0

for i in range(0,rows):
    for j in range(0,cols):
        print("Enter in rows:",i+1,"column:",j+1)
        matrix[i][j]=int(input())

print(matrix)