def getProcess(parcels, k):
    rem = k - len(parcels)
    parcels.sort()
    ans, cur = 0, 1
    i = 0
    while i < len(parcels) and rem:
        if cur == parcels[i]:
            i += 1
        else:
            ans += cur
            rem -= 1
        cur += 1
    while rem > 0:
        ans += cur
        cur += 1
        rem -= 1
    return ans

list1 = [6,5,4,1,3]
# number = input('Enter the number elements in the list')
# for i in range(int(number)):
#     val = input(f'Enter {i} value:')
#     list1.append(int(val))
# m = input('Enter the target value:')
print(getProcess(list1,7))