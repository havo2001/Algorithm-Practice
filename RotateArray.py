def rotate(nums, k):
    n = len(nums)
    ans = [0] * n
    for i in range(n):
        ans[(i + k) % n] = nums[i]
    return ans

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))

