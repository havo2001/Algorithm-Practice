def findTheArrayConcVal(nums):
    i = 0
    j = len(nums) - 1
    con_value = 0
    while i < j:
        con_value += int(str(nums[i]) + str(nums[j]))
        i += 1
        j -= 1
        if i == j:
            con_value += nums[i]
    return con_value

nums = [7,52,2,4]
print(findTheArrayConcVal(nums))