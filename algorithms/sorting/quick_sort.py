def partition(arr,low,high):
    pivot=arr[high]
    #pointer to swap values greater than pivot
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            (arr[j],arr[i])=(arr[i],arr[j])

    (arr[i+1],arr[high])=(arr[high],arr[i+1])
    return i+1

def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
arr=[5,6,4,3,2,1]
quick_sort(arr,0,len(arr)-1)
print(arr)
