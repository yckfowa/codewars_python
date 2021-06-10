def pipe_fix(nums):
    for i in range(nums[0], nums[-1] +1):
        if i not in nums:
            nums.append(i)
    nums.sort()
    return nums
