#wap to input 3 side of a triangke and print its type
x=int(input("Enter 1st side of the triangle :"))
y=int(input("Enter 2nd side of the triangle :"))
z=int(input("Enter 3rd side of the triangle :"))
if(x==y==z):
    print("This is equilateral triangle")
elif(x==y or y==z or z==y):
    print("This is Isoceles triangle")
else:
    print("This is scalene triangle")