#Concatenate two lists in the following order:
list1=[1,2]
list2=[4,5]
list3=[]
for i in list1:
    for j in list2:
        list3.append((i,j))
print(list3)