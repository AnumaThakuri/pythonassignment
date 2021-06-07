def sum(list,n):
    if len(list)==1:
        return list[0]
    else:
        return list[0]+sum(list[1:],n)
list=[]
list=[1,2,3,4,5]
n=len(list)

ans=sum(list,n)
print(ans)