def rearrange(nums):
    result = []

    for x, y in zip(nums[:len(nums) // 2], nums[len(nums) // 2:]):
        result.extend([x, y])

    return result