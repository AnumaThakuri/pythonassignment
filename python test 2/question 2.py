#wap to sort all the elements in ascending order using bubble sort
def bubblesort(array):
    L=len(array)
    for i in range(L):
        for j in range(0,L-i-1):
            if(array[j])>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
array=[5,1,4,2,8]
bubblesort(array)
print("sorted array is :")
for i in range(len(array)):
    print(array[i]) 