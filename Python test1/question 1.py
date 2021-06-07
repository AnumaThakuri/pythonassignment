#convert tempersture clesius to farenhuet and vice versa
farenheit=float(input("Enter the temperature : "))
celsius=(farenheit-32)*5/9
print(farenheit ," Farenheit is",celsius,"Celsius")
farenheit=(celsius*9/5)+32
print(celsius," Celsius is",farenheit,"Farenheit")