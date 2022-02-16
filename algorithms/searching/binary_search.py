def binarySearch(inputArr,low,hi,key):
    mid = (hi+low)//2
    if inputArr[mid]==key:
        return int(mid)
    elif key<inputArr[mid]:
        hi=mid-1
    elif key>inputArr[mid]:
        low=mid+1
    return binarySearch(inputArr,low,hi,key)

def main():
    input=[1,2,3,4,5,6]
    print(binarySearch(input,0,(len(input)-1),1))
main()
