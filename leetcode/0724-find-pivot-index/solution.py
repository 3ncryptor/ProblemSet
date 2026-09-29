# Runtime: 11 ms
# Memory: 20.2 MB

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            
            left += nums[i]

        return -1