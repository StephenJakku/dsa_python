def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        #temp arrays to store Left and Right partitions
        L=arr[:mid]
        R=arr[mid:]
        #Recursively call Left and Right to divide the problem into smaller sub-problems
        mergesort(L)
        mergesort(R)
        #Sorting the final sub-problems
        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        #check for left over elements
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr=[5,6,4,3,2,1]
mergesort(arr)
print(arr)
