def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1
    while (high >= low):
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if target > nums[mid]:
        return mid + 1
    return mid

print(searchInsert([1,2,3,4,5],6))