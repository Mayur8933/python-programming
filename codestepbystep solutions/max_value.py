def max_value(nums):
    count = len(nums)

    if count == 1:
        return nums[0]
    return max(nums)

max_value([17, 7, -1, 26, 3, 9])