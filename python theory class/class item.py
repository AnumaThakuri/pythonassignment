class item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    
    def purchase(self,quantity):
        self.quantity=self.quantity-quantity 
        print("number of item to be purchased :",quantity)
        print("quantity after a purchased :",self.quantity)
    
    def increaseStock(self,quantity):
        self.quantity=self.quantity+quantity
        print("Number of item to be added :",quantity)
        print("number of item in the stock :",self.quantity)

    def display(self):
        print("Name of the item :",self.name)
        print("Price of the item :",self.price)
        print("quantity of the item",self.quantity)

    def __lt__(self,other):
        if self.quantity<other.quantity:
            return True
        else:
            return False
    
def main():
    i1=item('Brush',20,25)
    i2=item('salt',25,23)
    #i3=item('pen',10,39)
    i1.purchase(14)
    i2.purchase(20)
    #i3.purchase(3)
    i1.increaseStock(90)
    i2.increaseStock(8)
    #i3.increaseStock(80)
    i1.display()
    i2.display()
    #i3.display()
    if(i1<i2):
        print('order1')
    else:
        print('order 2')

if __name__=='__main__':
    main()
