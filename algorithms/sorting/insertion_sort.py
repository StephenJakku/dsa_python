def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]

        j=i-1

        while key<arr[j] and j>=0:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

print(insertion_sort([2,3,1,8,4,2,8,2,1]))