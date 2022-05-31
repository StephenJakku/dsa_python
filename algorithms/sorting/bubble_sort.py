def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
    return arr

print(bubble_sort([6,5,4,3,2,1]))

                