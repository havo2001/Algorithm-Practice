def binarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while not (left > right):
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return -1





nums = [12]
target = 12
print(binarySearch(nums, target))