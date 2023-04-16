def longest_subarray(nums):
    begin = 0
    end = 1
    if len(nums) == 1:
        return 0

    max_value = 0
    current_sum = nums[begin]
    first = 0
    second = 0
    while end < len(nums):
        # print(str(begin) + " " + str(end) + " " + str(current_sum))
        val = current_sum + nums[end] + 1
        if val >= (end - begin + 1):
            if val > max_value:
                max_value = val - 1
                first = begin
                second = end
            current_sum = val - 1
            end += 1
        else:
            current_sum -= nums[begin]
            begin += 1

    if second - first + 1 == max_value:
        return max_value - 1
    return max_value


nums = [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1]
print(longest_subarray(nums))
