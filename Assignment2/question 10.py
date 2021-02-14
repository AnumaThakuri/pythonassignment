print("input lengths of the triangle :")
x=int(input("x :"))
y=int(input("y :")) 
z=int(input("z :"))
if x==y==z:
    print("The triangle is Equilateral triangle")
elif x==y or y==z or z==x:
    print("The triangle is Isoceles triangle")
else:
    print("The triangle is Scalene triangle")