'''concatenate two list in the following order:
input:L1=[1,2] L2=[4,5]
output:l3=[(1,2),(1,2),(2,4),(2,5)]'''

list1=[1,2]
list2=[4,5]
list3=[]
for i in list1:
    for j in list2:
        list3.append((i,j))
print(list3) 