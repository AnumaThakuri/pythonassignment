class Rectangle():
    def getdata(self,l,b):
        self.length=l
        self.breadth=b 
    def setlength(self,l):
        self.length=l
        print("The update length of the rectangle :",self.length)
    def setbreadth(self,b):
        self.breadth=b
        print("The updated breadth of the rectangle :",self.breadth)
    def area(self):
        print("area=",self.length*self.breadth)
    def perimeter(self):
        print("perimeter =",2*(self.length+self.breadth))
    
r1 = Rectangle()
r1.getdata(45,30)
r1.area()
r1.perimeter()
r2 = Rectangle()
r2.getdata(45,30)
r2.setlength(40)
r2.setbreadth(20)
r2.area()
