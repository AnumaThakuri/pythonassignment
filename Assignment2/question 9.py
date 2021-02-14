def calculateBill(units):
    if(units<=300):
        print("Monthly rent Rs.300 consumer has to pay minimun Rs:")
        return 300;
    elif(units>=301 and units<=800):
        return(300*7)+(units-300*9);
    elif(units>=801 and units<=1500):
        return ((300*7)+(500*9)+(units-800)*12);
    elif(units>1500):
        return((300*7)+(500*9)+(700*12)+(units-1500)*15);
units=int(input("Enter units no :"));
print(calculateBill(units));