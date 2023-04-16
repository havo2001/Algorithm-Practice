def maxSubArray(nums):
    i = 0
    j = 0
    max = -1001
    curr = 0
    for k in range(len(nums)):
        curr += nums[k]
        if curr > max:
            max = curr
            j = k + 1
        if curr < 0:
            curr = 0
            i = k + 1
            j = k + 1
    return nums[i: j]

nums = [5,4,-1,7,8]
print(maxSubArray(nums))




