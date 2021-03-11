L=[(1,2),(1,2),(2,3),(1,1),(3,8)]
L1=[]
i=0; j=0
#for i in range (len(L)):
while i<len(L):
    #print(L[i][0])
    city=L[i][0]
    rain=L[i][1]
    j=i+1
    c=1
    while j<len(L):
        if city==L[j][0]:
            rain=rain+L[j][1]
            c=c+1
            L.pop(j)
        else:
            j=j+1
    rain=rain/c
    L1.append((city,rain))
    i=i+1
print(L1)