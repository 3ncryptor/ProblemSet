# Runtime: 0 ms
# Memory: 20.7 MB

# from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return [seen[complement], idx]
            seen[val] = idx
        return []
