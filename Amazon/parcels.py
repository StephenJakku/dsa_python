def parcels(parcels,k):
    res=0
    count=0
    if len(parcels)==k:
        return 0
    for i in range(1,k+1):
       if i not in parcels:
            #print(i)
            res+=i
            count+=1
       if count == k-len(parcels):
           break
    return res

print(parcels([6,5,4,1,3],7))
