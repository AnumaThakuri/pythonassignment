def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+s[0]
s=input("Enter your string :")
print("The reverse of",s ," is :",reverse(s))