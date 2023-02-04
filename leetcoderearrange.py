class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half_length = n

        result = []

        for i in range(half_length):
            x = nums[i]
            y = nums[i + half_length]
            result.extend([x, y])

        return result
