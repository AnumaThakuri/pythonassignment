list1=[4,2,5,3]
list2=[90,33,11,24]
list3=list1+list2
print('list3 ->',list3)
 
for i in range(7):
    min_value=i
    for j in range(i+1,len(list3)):
        if[list3[j] < list3[min_value]]:
            min_value=j

temp=list3[i]
list3[i]=list3[min_value]
list3[min_value]=temp
print(list3)