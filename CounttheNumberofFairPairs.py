import bisect
def countFairPairs(nums, lower, upper):
    nums.sort()
    count = 0
    for i in range(len(nums)):
        a = bisect.bisect_left(nums, lower - nums[i])
        b = bisect.bisect_right(nums, upper - nums[i])
        if a < i < b:
            count += b - a - 1
        else:
            count += b - a
    return count // 2



nums = [1,7,9,2,5]
lower = 11
upper = 11

print(countFairPairs(nums, lower, upper))

