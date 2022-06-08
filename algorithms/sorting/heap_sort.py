def heapify(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    #check if l is greater than root
    if l<n and arr[largest]<arr[l]:
        largest = l
    # check if r is greater than root
    if r<n and arr[largest]<arr[r]:
        largest=r
    #if i is not largest, swap the root with largest and heapify the root recursively
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]

        heapify(arr,n,largest)


def heap_sort(arr):
    n=len(arr)
    #building a maxheap
    for i in range(n//2,-1,-1):
        heapify(arr,n,i)

    #Extract elements one by one
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)

inp=[5,4,3,2,6,7,1]
heap_sort(inp)
print(inp)